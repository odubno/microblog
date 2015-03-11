from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from sqlalchemy import event

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
