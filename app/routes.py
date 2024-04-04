from flask import render_template
from app import app

@app.route('/')
def home():
    user = {"username": "Pedro"}
    notes = [{'author': user, 'body': 'Beautiful day!'}, {'author': user, 'body': 'Beautiful night!'}]
    return render_template('home.html', title='Home', user=user, notes=notes)