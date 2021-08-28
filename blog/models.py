from blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.jpg')
    email = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(30), default='John Doe')
    password_hash = db.Column(db.String(128))
    member_since = db.Column(db.DateTime, default=datetime.utcnow)

    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, username, password):

        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password_hash, password)

    def __repr__(self):

        return f"Username: {self.username}"

class BlogPost(db.Model):

    __tablename__ = 'blogposts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date1 = db.Column(db.DateTime)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id, date1):

        self.title = title
        self.text = text
        self.user_id = user_id
        self.date1 = datetime.utcnow()

    def __repr__(self):

        return f"Post ID: {self.id} -- Title: {self.title}"
