from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
from wtforms.validators import InputRequired

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

@app.route('/cart')
def cart():
    return render_template('shoppingcart.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')


if __name__ == '__main__':
    app.run()