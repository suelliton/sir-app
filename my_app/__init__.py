from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from requests import get


 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['DEBUG'] = True







db = SQLAlchemy(app)
 
from my_app.views import coleta
app.register_blueprint(coleta) 

db.create_all()