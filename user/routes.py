from flask import Flask, render_template, request
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


@app.route('/user/updatepassword/', methods=['PUT'])
def update_password():
    return User().update_password()


@app.route('/mlmodel/uploadmodel/', methods=['POST'])
def upload_model():
    return MlModels().upload_model()


@app.route('/mlmodel/getmodel', methods=['GET'])
def get_model():
    return MlModels().get_model()


@app.route('/dashboard/summarizer/', methods=['POST'])
def get_summary():
     if request.method == 'POST':
         file = request.files['file']

         if file:                  
            text= str(file.read())
            print('inside try')
         else:
            t = request.form['text']
            text= str(t)
            print('inside except')
         #print(text)
         res = BERTSummarizer(text)
         #print(res)
         #return('Task Done')
         return render_template('summarizer_result.html', result =res)
