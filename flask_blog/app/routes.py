from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Hasanuzzaman'}
  posts = [
    { 'title': 'first post', 'des': 'First post description' },
    { 'title': '2nd post', 'des': '2nd post description' },
    { 'title': '3rd post', 'des': '3rd post description' },
  ]
  return render_template('index.html', user = user, title = 'my blog', posts = posts)

@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='login', form=form)  