from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

from flaskext.csrf import csrf

app = Flask(__name__)
#app.config.from_object('settings')
app.config.from_object(os.environ['APP_SETTINGS'])

csrf(app)

# Database stuff
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Is it here?

from thisapi import main
