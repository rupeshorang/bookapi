# Configuration for database
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bookdb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
