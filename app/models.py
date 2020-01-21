from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hint = db.Column(db.String(140))
    password_hash = db.Column(db.String(128))

    def get_password_hint(self):
        return self.password_hint

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def set_password_hint(self, newhint):
        self.password_hint = newhint

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Submission(db.Model):
    ident = db.Column(db.Integer, primary_key=True)
    publishing_status = db.Column(db.String(20), default="new")
    submission = db.Column(db.Unicode(10000))
    submitter = db.Column(db.Unicode(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    title = db.Column(db.Unicode(140))

    def set_status(self, status):
        self.publishing_status = status

    def __repr__(self):
        return '<Submission {}'.format(self.submission)
