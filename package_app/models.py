from datetime import datetime
from package_app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def user_loder(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    packages = db.relationship('Package', backref='sender', lazy=True)

    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.username,
                                           self.email,
                                           self.image_file)

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wheight = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    diliverd_at = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reclamations = db.relationship('Reclamation', backref='pack')

    def __repr__(self):
        return "Package('{}', '{}', '{}', '{}')".format(self.id,
                                                  self.created_at,
                                                  self.diliverd_at,
                                                  self.price)
    
    
class Reclamation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)

    def __repr__(self):
        return "Reclamation('{}', '{}', '{}')".format(self.id,
                                                  self.description,
                                                  self.status)

