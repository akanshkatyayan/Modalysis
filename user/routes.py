from tokenize import Name
from flask import Flask, render_template, request
from requests import session
from app import app
from app import db
from user.models import User
from mlmodels.model_api import MlModels
from user.summary import BERTSummarizer
from datetime import datetime
from io import BytesIO
from flask import Flask, render_template, request, send_file



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

@app.route('/dashboard/summarizer/', methods=['POST', 'GET'])
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
         db.user_history.insertOne(
            { "name" : session.get('name'),
              "File_before_summary" : text,
              "File_after_summary" : res,
     
             })

         #print(res)
        #return('Task Done')
         return render_template('summarizer_result.html', result =res)
     elif request.method == 'GET':
         Name= db.user.find({'name':session.get('name')})
         Files= db.user_history.find()
         return Name, Files

         

