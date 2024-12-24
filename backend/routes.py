from flask import request, jsonify
from app import app
from google_oauth import verify_google_token

@app.route('/api/login', methods=['POST'])
def login():
    token = request.json.get('token')

    if not token:
        return jsonify({'message': 'No token provided'}), 400

    user = verify_google_token(token)

    if user:
        return jsonify({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name
        }), 200
    else:
        return jsonify({'message': 'Invalid Credentials'}), 401