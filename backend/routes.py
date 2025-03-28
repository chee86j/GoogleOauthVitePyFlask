from flask import redirect, url_for, session, jsonify, Blueprint, request
from flask_dance.contrib.google import google
from flask_login import login_user, current_user
from .models import User
from .extensions import db
import os
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta
from .utils.images import url_to_base64, validate_image, compress_image
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/auth/google', methods=['POST'])
def google_auth():
    try:
        data = request.json
        if not data or 'credential' not in data or 'userInfo' not in data:
            return jsonify({'error': 'Missing required data'}), 400

        # Extract user info from the response
        email = data['userInfo'].get('email')
        first_name = data['userInfo'].get('given_name', '')
        last_name = data['userInfo'].get('family_name', '')
        picture_url = data['userInfo'].get('picture')
        
        logger.info("Processing Google login for email: %s", email)

        if not email:
            return jsonify({'error': 'Email not found in user info'}), 400

        # Convert profile picture to base64 if available
        avatar = None
        if picture_url:
            try:
                avatar = url_to_base64(picture_url)
                logger.info("Successfully converted profile picture to base64")
            except Exception as e:
                logger.error("Failed to convert profile picture: %s", str(e))
                # Continue without avatar rather than failing the whole login

        # Check if user exists
        user = User.query.filter_by(email=email).first()

        if not user:
            # Create new user if doesn't exist
            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                avatar=avatar
            )
            db.session.add(user)
            logger.info("Created new user with avatar: %s", bool(avatar))
        else:
            # Update existing user's info
            user.first_name = first_name
            user.last_name = last_name
            if avatar and avatar != user.avatar:
                user.avatar = avatar
                logger.info("Updated existing user's avatar")
                
        db.session.commit()
        
        user_dict = user.to_dict()
        logger.info("Sending user data: id=%s, email=%s, has_avatar=%s",
                   user_dict.get('id'),
                   user_dict.get('email'),
                   bool(user_dict.get('avatar')))

        # Create access token
        access_token = create_access_token(
            identity=email,
            expires_delta=timedelta(days=1)
        )

        return jsonify({
            'access_token': access_token,
            'user': user_dict
        }), 200

    except Exception as e:
        logger.error("Unexpected error in google_auth: %s", str(e))
        return jsonify({'error': str(e)}), 500

@auth_routes.route('/auth/verify', methods=['GET'])
@jwt_required()
def verify_token():
    try:
        current_user_email = get_jwt_identity()
        user = User.query.filter_by(email=current_user_email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        user_dict = user.to_dict()
        logger.info("Verify endpoint - user data: id=%s, email=%s, has_avatar=%s",
                   user_dict.get('id'),
                   user_dict.get('email'),
                   bool(user_dict.get('avatar')))
            
        return jsonify({
            'user': user_dict
        }), 200
        
    except Exception as e:
        logger.error("Verify endpoint error: %s", str(e))
        return jsonify({'error': str(e)}), 500