from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from. import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    order_id = db.Column(db.Integer,db.ForeignKey("orders.id"))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)    


    def __repr__(self):
        return f'User {self.username}'
                
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'               
class Pizza(db.Model):

    __tablename__ = 'pizzas'

    all_pizza=[]

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    pic_path = db.Column(db.String())
    size = db.Column(db.String)
    price_large = db.Column(db.Integer)
    price_small = db.Column(db.Integer)

    def save_pizza(self):
        db.session.add(self)
        db.session.commit()    


class Order(db.Model):
    __tablename__ = 'orders'
    
    all_orders = []

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),index = True)
    size = db.Column(db.String(255),index = True)
    toppings = db.Column(db.String(255),index = True)
    no_of_pizzas = db.Column(db.Integer,index = True)
    users = db.relationship('User',backref = 'order',lazy="dynamic")

    def save_order(self):
        db.session.add(self)
        db.session.commit()    

    def __repr__(self):
        return '<Order %r>' % self.name



    