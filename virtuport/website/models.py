from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func # Added for func.now()


DATABASE_URL = "postgresql+psycopg2://postgres:akul@localhost:5432/akul"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SQLAlchemy()
Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter_by(email=email, password=password).first()
        if user and check_password_hash(user.password, password):
            return user
        return None

class ContactSubmission(db.Model):
    __tablename__ = 'contact' # Table name is 'contact' as specified
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<ContactSubmission {self.name}>'

Base.metadata.create_all(bind=engine)