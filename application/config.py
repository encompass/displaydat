"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    DISPLAY_TIMEZONE = environ.get('DISPLAY_TIMEZONE')

class DevConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'