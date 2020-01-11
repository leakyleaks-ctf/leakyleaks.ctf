import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'Eezai4yairoow5fohZ3vaSh7tu7shae7ie'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'leaks.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
