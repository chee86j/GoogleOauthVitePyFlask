from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from .extensions import db, jwt

# Load environment variables
load_dotenv()

# For development only - allows OAuth over HTTP
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def create_app():
    app = Flask(__name__)
    
    # Configure CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": os.getenv('FRONTEND_URL', 'http://localhost:5173'),
            "supports_credentials": True
        }
    })

    # Set additional headers for CORS
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Cross-Origin-Opener-Policy', 'same-origin-allow-popups')
        return response

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    # Import routes
    from .routes import auth_routes
    app.register_blueprint(auth_routes, url_prefix='/api')

    # Create database tables
    with app.app_context():
        db.create_all()

    @app.route('/api/health')
    def health_check():
        return {'status': 'healthy'}, 200

    return app 