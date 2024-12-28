from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    google_id = db.Column(db.String(100), unique=True)

    def __init__(self, first_name, last_name, email, google_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.google_id = google_id

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"