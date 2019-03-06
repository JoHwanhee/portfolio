"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
@app.route('/about')
def home():
    return render_template(
        'about.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/experience')
def experience():
    return render_template(
        'experience.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/education')
def education():
    return render_template(
        'education.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/skills')
def skills():
    return render_template(
        'skills.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/interests')
def interests():
    return render_template(
        'interests.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/awards')
def awards():
    return render_template(
        'awards.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
