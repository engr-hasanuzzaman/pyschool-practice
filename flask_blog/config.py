import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('secrete_key') or 'My supre secrete key'
  TEMPLATES_AUTO_RELOAD = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_UR') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  