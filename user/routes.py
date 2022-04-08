from flask import Flask
from app import app
from user.models import User
from mlmodels.model_api import MlModels


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/user/updatepassword/', methods=['PUT'])
def update_password():
    return User().update_password()


@app.route('/mlmodel/uploadmodel/', methods=['POST'])
def upload_model():
    return MlModels().upload_model()