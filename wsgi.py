import os

from application.app import create_app

print(os.environ)
app = create_app(os.environ.get('FLASK_CONFIG') or 'default')