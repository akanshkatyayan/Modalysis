from flask import Flask, render_template, session, redirect
import pymongo
import dns
from functools import wraps
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.debug = True
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
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    # render template to display this html page on app.route /
    return render_template("aboutus.html")


@app.route('/dashboard/')
@login_required
def dashboard():
    # render template to display this html page on app.route /dashboard/
    if session['user']['role'] == "admin":
        return render_template("admindashboard.html")
    return render_template("userdashboard.html")


@app.route('/dashboard/summarizer/')
@login_required
def summarizer():
    # render template to display this html page on app.route /dashboard/
    return render_template("summarizer.html")


@app.route('/signup/')
def register():
    # render template to display signup page for new user
    return render_template("signup.html")


@app.route('/dashboard/computeimage/')
def compute_engine():
    # render template to display to Compute Engine Page
    return render_template("computeengineapi.html")


@app.route('/dashboard/updatepassword/')
def updatepassword():
    # render template to display to Compute Engine Page
    return render_template("updatepassword.html")


@app.route('/dashboard/uploadmlmodel/')
def upload_mlmodel():
    # render template to display to Compute Engine Page
    return render_template("uploadmlmodel.html")

