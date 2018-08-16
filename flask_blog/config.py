import os

class Config:
  SECRET_KEY = os.environ.get('secrete_key') or 'My supre secrete key'
  TEMPLATES_AUTO_RELOAD = True