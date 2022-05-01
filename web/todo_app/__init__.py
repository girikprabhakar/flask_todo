from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from todo_app.config import DEV_DB, PROD_DB

app = Flask(__name__)
if os.getenv('DEBUG') == '1':
    app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)