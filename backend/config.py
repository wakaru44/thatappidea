import os
basedir = os.path.abspath(os.path.dirname(__file__))

def get_env(keyname):
    """ Get a key from the environment variables"""
    try:
        value = os.environ[keyname]
        return value
    except KeyError as e:
        print "WARN: Environment variable not set: {0}".format(keyname)
    return None


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = get_env('DATABASE_URL') or 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
