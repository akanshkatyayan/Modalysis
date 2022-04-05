from flask import Flask, request
from app import app
from user.models import User
from mlmodels.model_api import MlModels
from user.summary import BERTSummarizer


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

@app.route('/dashboard/summarizer/', methods=['POST'])
def get_summary():
     if request.method == 'POST':
        file = request.files['file']
        text= str(file.read())
        print(text)
        res = BERTSummarizer(text)
        print(res)
        return('Task Done')




