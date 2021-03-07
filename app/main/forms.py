from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,SelectField,TextAreaField
from wtforms.validators import Required,Email
from flask_wtf.file import FileField

class OrderForm(FlaskForm):
    email = StringField('Enter email to recieve reciept', validators=[Required(), Email()] )
    size = SelectField('Choose Pizza size', choices = [('Large','Large'),('Small','Small')],validators=[Required()])    
    toppings = SelectField('Choose toppings', choices = [('onions','onions'),('mushroom','mushroom'),('sausage','sausage'),('Gorgonzola and mushroom','Gorgonzola and mushroom'),('Gorgonzola and radicchio','Gorgonzola and radicchio'),('sausage and kale','sausage and kale')])
    no_of_pizzas = IntegerField('Enter number of pizzas', validators=[Required()])
    submit = SubmitField('Order Now')
    

class PizzaForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    price_small = IntegerField('Price-Small',validators=[Required()])  
    price_large = IntegerField('Price-Large',validators=[Required()])  
    submit = SubmitField('Add Pizza')
       