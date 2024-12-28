from app import db, app
from models import User
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_db():
    db.drop_all()
    db.create_all()

def seed_database():
    # Clear existing users
    User.query.delete()
    
    # Create sample users
    sample_users = [
        User(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            google_id="987654321"
        )
    ]
    
    try:
        db.session.add_all(sample_users)
        db.session.commit()
        print("Users seeded successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding users: {e}")

if __name__ == '__main__':
    with app.app_context():
        try:
            init_db()
            seed_database()
            print("Database seeded successfully!")
        except Exception as e:
            print(f"Error during database seeding: {e}")