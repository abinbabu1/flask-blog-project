from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from blog.models import User

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_email(self, email):

        if not User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Invalid email!')

class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):

        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been already registered')

    def validate_username(self, username):

        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been already registered')

class UpdateUserForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['png','jpg'])])
    submit = SubmitField('Update')

    def validate_email(self, email):

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            if user.email == current_user.email:
                pass
            else:
                raise ValidationError('Email has been already registered')


    def validate_username(self, username):

        user = User.query.filter_by(username=self.username.data).first()
        if user:
            if user.username == current_user.username:
                pass
            else:
            #if User.query.filter_by(username=self.username.data).first():
                raise ValidationError('Username has been already registered')
