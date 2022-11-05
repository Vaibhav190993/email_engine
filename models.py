from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    # email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = bcrypt.generate_password_hash(password).decode('utf-8')

class SendMail(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    send_date = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return f"Email('{self.message}', '{self.send_date}')"

