from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from ..models import User,Admin
from wtforms import ValidationError

class LoginFormUser(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationFormUser(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password2',message = 'Passwords must match')])
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginFormAdmin(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    admin_id = StringField('Enter your id')
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationFormAdmin(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password2',message = 'Passwords must match')])
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    admin_id = StringField('Enter your id')
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if Admin.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if Admin.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

    def validate_admin_id(self,data_field):
        if Admin.query.filter_by(admin_id = data_field.data).first():
            raise ValidationError('That id has an account already')    
