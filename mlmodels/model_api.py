from flask import Flask, jsonify, request, session, flash
import pymongo
from app import db
import pickle
import pandas as pd
import time


class MlModels:

    def get_model(self, model_name):
        json_data = {}
        # Read requested model from database
        data = db.model_pickle_files.find({'name': model_name})

        for i in data:
            json_data = i
        # fetching model from db
        pickled_model = json_data[model_name]

        return pickle.loads(pickled_model)

    def upload_model(self):

        """
        Function to upload ML Model to MongoDB
        """
        # model_name = request.form.get('modelname')
        # print(model_name)
        # inputfile = request.files['file']
        # print(inputfile.filename)
        # pickle_object = pd.read_pickle(inputfile)
        #
        #
        # result = db.model_pickle_files.insert_one({model_name: pickle_object, 'name': model_name, 'created_time': time.time()})
        # flash("Model {} saved with Id: {}".format(model_name, result.inserted_id))
        #
        return jsonify("test", 200)


    def train_model(self, model_name, train_data):
        pass

    def evaluate_model(self, model_name, test_data):
        pass

