from flask import Flask, jsonify
import pymongo
from app import db
import pickle


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

    def train_model(self, model_name, train_data):
        pass

    def evaluate_model(self, model_name, test_data):
        pass
