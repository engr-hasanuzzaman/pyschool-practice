from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
  user = {'username': 'Hasanuzzaman'}
  posts = [
    { 'title': 'first post', 'des': 'First post description' },
    { 'title': '2nd post', 'des': '2nd post description' },
    { 'title': '3rd post', 'des': '3rd post description' },
  ]
  return render_template('index.html', title = 'my blog', posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
      return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user is None or not user.check_password(form.password.data):
          flash('Invalid username or password')
          return redirect(url_for('login'))
      login_user(user, remember=form.remember_me.data)
      return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    redirect(url_for('index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username = form.username.data, email = form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Congratulation, your registration is complete')
    return redirect(url_for('login'))
  return render_template('register.html', form=form, title='registration')

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username = username).first_or_404()
  posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
  return render_template('user.html', user=user, posts=posts)
