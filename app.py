from flask import Flask, render_template, session, redirect
import pymongo
import dns
from functools import wraps
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.secret_key=config.get('main', 'secret_key')

# Database
db_connection_stmt = config.get('main', 'db_command')
client = pymongo.MongoClient(db_connection_stmt)
db = client.ModalysisDatabase


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


# Routes
from user import routes


@app.route('/')
def home():
    # render template to display this html page on app.route /
    return render_template("home.html")


@app.route('/dashboard/')
@login_required
def dashboard():
    # render template to display this html page on app.route /
    return render_template("dashboard.html")