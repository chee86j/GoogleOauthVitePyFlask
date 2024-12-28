from google.oauth2 import id_token
from google.auth.transport import requests
import os
from models import User
from extensions import db

def verify_google_token(token):
    try:
        # Make sure GOOGLE_CLIENT_ID is available in .env
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        if not client_id:
            raise ValueError('GOOGLE_CLIENT_ID not found in environment variables')

        idinfo = id_token.verify_token(token, requests.Request(), client_id)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        user_google_id = idinfo['sub']
        user_email = idinfo['email']
        user_first_name = idinfo['given_name']
        user_last_name = idinfo['family_name']

        # Check if email is verified
        if not idinfo.get('email_verified'):
            raise ValueError('Email not verified by Google.')

        user = User.query.filter_by(google_id=user_google_id).first()

        if user:
            return user
        else:
            new_user = User(
                first_name=user_first_name,
                last_name=user_last_name,
                email=user_email,
                google_id=user_google_id
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user
        
    except ValueError as e:
        # Invalid token
        print(f"ValueError: {e}")
        return None