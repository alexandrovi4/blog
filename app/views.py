__author__ = 'kirill'

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "this is test page"
