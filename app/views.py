__author__ = 'kirill'
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

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
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember'] = form.remember.data
        return oid.try_login(form.openid.data, ask_for=['nickname','email'])
    return render_template('login.html',
                           title='Sign in',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember = False
    if 'remember' in session:
        remember = session['remember']
        session.pop('remember', None)
    login_user(user, remember = remember)
    return redirect(request.args.get('next') or url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

