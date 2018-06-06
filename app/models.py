# third-party imports
from datetime import datetime

# local imports
from app import db

class User(db.Model):
    """
    Create a User table
    """

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_updated = db.Column(db.DateTime, nullable=True, onupdate=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.email
