from flask import render_template 
from app import app 
from app.forms import LoginForm

@app.route('/') 
@app.route('/index') 
def index(): 
    user = {'username': 'Wayne McCoy'} 
    posts = [ 
        { 'author': {'username': 'Geo'}, 'body': 'We have flowmarks' }, 
        { 'author': {'username': 'Keith'}, 'body': 'The Avengers movie was so cool!' },
        { 'author': {'username': 'Mike'}, 'body': 'Get the fucking line running'} 
    ] 
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)