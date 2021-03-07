from flask import render_template,flash, url_for, redirect
from . import main
from .forms import OrderForm,PizzaForm
from flask_login import login_required,current_user
from .. import db,photos
from ..models import Pizza,Order


@main.route('/')
def index():
    title = 'PIZZA HUB'
    pizza = Pizza.query.all()
    return render_template('index.html', title =title, pizza=pizza)



@main.route('/order', methods =['GET', 'POST'])
@login_required
def order():
    form = OrderForm()

    if form.validate_on_submit():

        order = Order(email = form.email.data, size = form.size.data, toppings = form.toppings.data, no_of_pizzas = form.no_of_pizzas.data)
        order.save_order()

        title = "New Order"
        return redirect(url_for('main.cart'))


    title = 'Ordering form'
    return render_template('order.html', form =  form, title = title)

@main.route('/pizza', methods =['GET', 'POST'])
def pizza():
    form = PizzaForm()

    if form.validate_on_submit():

        name = Pizza(name = form.name.data, price_small = form.price_small.data,price_large = form.price_large.data)
        name.save_pizza()

        title = "New Order"
        return redirect(url_for('main.update_pic'))

    title = 'Pizza form'
    return render_template('pizza/pizza.html', form =  form, title = title)

@main.route('/pizza', methods =['GET', 'POST'])
def update_pic(name):
    form = PizzaForm
    pizza = Pizza.query.filter_by(name = form.name.data).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        pizza.pic_path = path
        db.session.commit()
    return redirect(url_for('main.pizza',name=name,pizza = pizza))

@main.route('/cart', methods =['GET','POST'])
def cart():

    title = 'CART'
    orders = Order.query.all()
    return render_template('cart.html', title =title, orders = orders,user=current_user)   