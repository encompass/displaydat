"""Flask configuration."""
# Learn about it here... https://flask.palletsprojects.com/en/2.2.x/config/
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    LOCAL_TIMEZONE = environ.get('LOCAL_TIMEZONE')


class DevConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    TRELLO_API_KEY = environ.get('TRELLO_API_KEY')
    TRELLO_API_TOKEN = environ.get('TRELLO_API_TOKEN')
    TRELLO_LIST_ID = environ.get('TRELLO_LIST_ID')