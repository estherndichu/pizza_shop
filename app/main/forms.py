from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Required,Email


class OrderForm(FlaskForm):
    email = StringField('Enter email to recieve reciept', validators=[Required(), Email()] )
    size = StringField('Size', validators=[Required()])
    toppings = StringField('Toppings', validators=[Required()])
    no_of_pizzas = IntegerField('Enter number of pizzas', validators=[Required()])
    submit = SubmitField('Order Now')