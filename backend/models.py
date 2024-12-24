from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    google_id = db.Column(db.String(255), unique=True, nullable=True)

    def __init__(self, first_name, last_name, email, google_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.google_id = google_id

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"