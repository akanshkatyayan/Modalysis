from flask import Flask, render_template, request
from discord_webhook import DiscordWebhook, DiscordEmbed
from app import app
from user.models import User
from mlmodels.model_api import MlModels
from user.summary import BERTSummarizer
import configparser
config = configparser.ConfigParser()
config.read('config.ini')


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


@app.route('/dashboard/uploadmlmodel/', methods=['GET', 'POST'])
def upload_model():
    if request.method == 'POST':
        modelname = request.form.get('modelname')
        print(modelname)
        file = request.files['inputmodel']
        print(file.filename)
        if file:
            print(file.filename)

    return render_template('uploadmlmodel.html')
    #return MlModels().upload_model()


@app.route('/mlmodel/getmodel', methods=['GET'])
def get_model():
    return MlModels().get_model()


@app.route('/dashboard/summarizer/', methods=['POST'])
def get_summary():
     if request.method == 'POST':
         file = request.files['file']

         if file:                  
            text= str(file.read())
            print('inside if')
         else:
            t = request.form['text']
            text = str(t)
            print('inside else')
         # print(text)
         res = BERTSummarizer(text)

         webhook = DiscordWebhook(url=config.get('main','webhook'), content='Your Text Summary is Ready...')
         webhook.add_file(file=res, filename='summary.txt')
         webhook.execute()
         
         # print(res)
         # return('Task Done')
         return render_template('summarizer.html', result=res)


# ---------------------User Management--------------------- #

@app.route('/user/createuser', methods=['POST'])
def createuser():
    return User().createuser()


@app.route('/user/deleteuser', methods=['DELETE'])
def deleteuser():
    return User().deleteuser()


@app.route('/user/updateuser', methods=['PUT'])
def updateuser():
    return User().updateuser()


@app.route('/user/getusers', methods=['GET'])
def getusers():
    return User().getusers()