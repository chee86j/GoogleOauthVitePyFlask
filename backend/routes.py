from flask import redirect, url_for, session, jsonify
from flask_dance.contrib.google import google
from flask_login import login_user, current_user
from app import app, db
from models import User
import os

@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    return redirect(url_for("google_authorized"))

@app.route('/google_authorized')
def google_authorized():
    if not google.authorized:
        return redirect(url_for('google_login'))
    
    try:
        # Fetch user information from Google
        resp = google.get("/oauth2/v1/userinfo")
        if not resp.ok:
            return jsonify({'error': 'Failed to fetch user info from Google.'}), 400

        user_info = resp.json()
        email = user_info["email"]
        first_name = user_info.get("given_name", "")
        last_name = user_info.get("family_name", "")
        google_id = user_info["id"]

        # Check if the user already exists
        user = User.query.filter_by(google_id=google_id).first()

        if not user:
            # Create a new user if not found
            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                google_id=google_id
            )
            db.session.add(user)
            db.session.commit()

        # Log the user in
        login_user(user)
        session['user'] = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        session.modified = True

        return redirect(f"{os.getenv('FRONTEND_URL')}?login=success")

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/check-auth')
def check_auth():
    if 'user' in session:
        return jsonify(session['user'])
    return jsonify({'error': 'Not authenticated'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    # Clear the session
    session.clear()
    return jsonify({'message': 'Successfully logged out'}), 200