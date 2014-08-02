__author__ = 'kirill'
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nick': 'Xy9se'} # fake
    posts = [
        {
            'author': {'nickname':'John'},
            'body':'beautiful day in Portland'
        },
        {
            'author':{'nickname':'Tom'},
            'body':'Hi. How do you fly?'
        }
    ]

    return render_template("index.html",
                           title="Home",
                           user=user,
                           posts=posts
                           )
