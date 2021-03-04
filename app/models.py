<<<<<<< HEAD
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    def __init__(self,username,email,password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    bio = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')


    def __repr__(self):
        return f'User {self.username}'



class Pizza(db.Model):

    __tablename__ = 'pizza'
    all_pizzas = []

    def __init__(self,id,pizza_title,image_path,description,user):
        self.id = id
        self.pizza_title = pizza_title
        self.image_path = image_path
        self.description = description
        self.user = user

    id = db.Column(db.Integer,primary_key = True)
    pizza_title = db.Column(db.String)
    image_path = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
=======
>>>>>>> views
