from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Boolean
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
	self.username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
	self.email = StringField('Email', validators=[DataRequired(), Length(min=2,max=20), Email()])
	self.password = PasswordField('Password', validators=[DataRequired()])
	self.confirm_password = PasswordField('Password', validators=[DataRequired()])
	self.submit = SubmitField('Register')


class LoginForm(FlaskForm):
	self.email = StringField('Email', validators=[DataRequired(), Length(min=2,max=20), Email()])
	self.password = PasswordField('Password', validators=[DataRequired()])
	self.remember = BooleanField('Remember Me')
	self.submit = SubmitField('Login')