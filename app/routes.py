from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
def home():
    user = {"username": "Pedro"}
    notes = [{'author': user, 'body': 'Beautiful day!'}, {'author': user, 'body': 'Beautiful night!'}]
    return render_template('home.html', title='Home', user=user, notes=notes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember={form.remember.data}')
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)