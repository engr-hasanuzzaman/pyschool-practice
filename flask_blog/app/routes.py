from flask import render_template, flash, redirect
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)