from flask import Flask
from flask import render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# flask forms imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# form validation imports
from wtforms.validators import Length, EqualTo, Email, DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# secret key
app.config['SECRET_KEY'] = '57798ed544580fcb365fa3c7'

db = SQLAlchemy(app)

# flask forms(in same file only cuz this is for learning)
class RegisterForm(FlaskForm):
    # render_kw allows to set html element attributes
    username = StringField(label='Username:', validators=
    [Length(min=2, max=30), DataRequired()], render_kw={'autofocus':True})
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6),
    DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=
    [EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

# models
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    def __repr__(self):
        return f'{self.username}'

# routes

# methods argument is required for post requests
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    # create form instance
    form = RegisterForm()
    # once the submit button is triggered
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_hash=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('home'))

    if form.errors != {}: # if the dict is not empty of errors
        for err_msg in form.errors.values():
            print("errors:", err_msg)

    return render_template('register.html', form=form)

@app.route('/')
def home():
    return 'homepage'
