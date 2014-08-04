__author__ = 'kirill'
from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="'+form.openid.data+'", remember_me='+str(form.remember.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign in',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
