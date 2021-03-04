from flask import render_template,flash, url_for, redirect
from app import app
from app.forms import RegistrationForm, LoginForm


@app.route('/')
def index():
    title = 'PIZZA HUB'
    return render_template('index.html', title =title)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    title = 'registration form'

    return render_template('register.html', title = title, form = form)

@app.route('/login', methods =['GET', 'POST'])
def login():
    form = LoginForm()

    title = 'login form'
    return render_template('login.html', form = form, title = title)


@app.route('/order', methods =['GET', 'POST'])
def order():
    form = OrderForm()

    title = 'Ordering form'
    return render_template('order.html', form =  form, title = title)