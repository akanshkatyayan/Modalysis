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


@app.route('/mlmodel/getmodel', methods=['GET'])
def get_model():
    return MlModels().get_model()
