from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField
from wtforms.fields import FieldList, FormField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SubmitForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=10, max=140)])
    submitter = StringField('Submitter', validators=[Length(min=0, max=500)])
    submission = TextAreaField('Submission', validators=[Length(min=30, max=10000)])
    submit = SubmitField('Submit')

class DashboardDetailForm(FlaskForm):
    action = RadioField(choices=[ ('new', 'New'), ('unpublished','Unpublished'), ('published','Published'), ('review', 'Review'), ('reviewed', 'Reviewed'), ('delete','Delete')])
#    action = RadioField(choices=[])
    submit = SubmitField('Change Status')

class AdminProfileForm(FlaskForm):
    password_hint = StringField('Your password hint:', validators=[Length(min=0, max=140)]) 
    old_password = StringField('Old password:', validators=[Length(min=0, max=140)]) 
    new_password = StringField('New password:', validators=[Length(min=0, max=140)]) 
    new_password2 = StringField('Repeat new password:', validators=[Length(min=0, max=140)]) 
    change_hint = SubmitField('Change Hint')
    change_password = SubmitField('Change Password')
