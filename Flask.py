from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask
from pywebio.input import *
from pywebio.output import *


from flask import Flask, jsonify, request
from preprocessing.functions import tokenize
import xgboost as xgb
import joblib
from healthcheck import HealthCheck
import six

import os
import logging

app = Flask(__name__)

logging.basicConfig(format='%(message)s', level=logging.INFO)
app = Flask(__name__)

target={0:'Debt collection', 1:'Mortgage', 2:'Credit card',3:'Bank account or service', 4:'Student loan'}
tfvectorizer = joblib.load('model/vectorizer.pkl') 
xgb_clf = xgb.Booster({'nthread': 3})
xgb_clf.load_model('model/xgb.model')

logging.info('All models loaded succcessfully')

def scorer(text):
   encoded_text = tfvectorizer.transform([text])
   score = xgb_clf.predict(xgb.DMatrix(encoded_text))
   return score

def predict():
    text= input("Enter complain", required=True)
    logging.info('Received incoming message - '+ text)
    predictions = scorer(text)
    predictions = predictions.argmax(axis=1)[0]
    str_predictions= str(predictions)
    category = target.get(predictions)
    put_text("complain:",str_predictions)
    put_text("category of the complain:",category)


app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])

app.run(host='localhost', port=80)