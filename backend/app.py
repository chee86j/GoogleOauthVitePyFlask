from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

db = SQLAlchemy(app)
CORS(app, resources={r"/*": {"origins": os.getenv('FRONTEND_URL')}})

import models
import routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # creates the databases
    app.run(debug=True, port=8000) #Run on port 8000