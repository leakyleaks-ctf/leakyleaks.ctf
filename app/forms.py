from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SubmitForm(FlaskForm):
    submitter = StringField('Submitter', validators=[Length(min=0, max=500)])
    submission = TextAreaField('Submission', validators=[Length(min=30, max=500)])
    submit = SubmitField('Submit')
