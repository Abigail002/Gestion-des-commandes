from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app.config['SECRET_KEY'] = 'hfhfffhdnx234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/order-dba'
app.config['SQLALCHEMY_TRACK_MODEIFICATIONS_URI'] = True

db = SQLAlchemy(app)
