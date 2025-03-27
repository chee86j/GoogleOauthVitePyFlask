from flask import redirect, url_for, session, jsonify, Blueprint, request
from flask_dance.contrib.google import google
from flask_login import login_user, current_user
from .models import User
from .extensions import db
import os
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta

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

        if not email:
            return jsonify({'error': 'Email not found in user info'}), 400

        # Check if user exists
        user = User.query.filter_by(email=email).first()

        if not user:
            # Create new user if doesn't exist
            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            db.session.add(user)
            db.session.commit()

        # Create access token
        access_token = create_access_token(
            identity=email,
            expires_delta=timedelta(days=1)
        )

        return jsonify({
            'access_token': access_token,
            'user': user.to_dict()
        }), 200

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@auth_routes.route('/auth/verify', methods=['GET'])
@jwt_required()
def verify_token():
    try:
        current_user_email = get_jwt_identity()
        user = User.query.filter_by(email=current_user_email).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
            
        return jsonify({
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500