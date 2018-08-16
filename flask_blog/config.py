import os

class Config:
  SECRETE_KEY = os.environ.get('secrete_key') or 'My supre secrete key'
  TEMPLATES_AUTO_RELOAD = True