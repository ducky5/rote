from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
# flask forms imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# secret key
app.config['SECRET_KEY'] = '57798ed544580fcb365fa3c7'

db = SQLAlchemy(app)

# flask forms(in same file only cuz this is for learning)
class RegisterForm(FlaskForm):
    # render_kw allows to set html element attributes
    username = StringField(label='Username:', render_kw={'autofocus':True})
    email = StringField(label='Email:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')

# models
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

# routes
@app.route('/register')
def register_page():
    # create form instance
    form = RegisterForm()

    return render_template('register.html', form=form)
