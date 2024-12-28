from flask import Flask, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import LoginManager, login_user, current_user
from dotenv import load_dotenv
import os
from flask_cors import CORS
from config import GoogleAuthConfig

# Load environment variables
load_dotenv()

# For development only - allows OAuth over HTTP
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = os.getenv('JWT_SECRET_KEY')

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@localhost/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

# Set up Google OAuth
google_bp = make_google_blueprint(
    client_id=GoogleAuthConfig.GOOGLE_CLIENT_ID,
    client_secret=GoogleAuthConfig.GOOGLE_CLIENT_SECRET,
    scope=["https://www.googleapis.com/auth/userinfo.email",
           "https://www.googleapis.com/auth/userinfo.profile",
           "openid"]
)
app.register_blueprint(google_bp, url_prefix="/login")

CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})

# Import routes after extensions initialization
from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=5000)
