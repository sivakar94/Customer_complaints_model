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

target={0:'Debt collection', 1:'Mortgage', 2:'Credit card',3:'Bank account or service', 4:'Student loan'}
tfvectorizer = joblib.load('model/vectorizer.pkl') 
xgb_clf = xgb.Booster({'nthread': 3})
xgb_clf.load_model('model/xgb.model')

logging.info('All models loaded succcessfully')

def scorer(text):
   encoded_text = tfvectorizer.transform([text])
   score = xgb_clf.predict(xgb.DMatrix(encoded_text))
   return score

@app.route('/score', methods=['POST'])
def predict_fn():
    text = request.get_json()['text']
    logging.info('Received incoming message - '+ text)
    predictions = scorer(text)
    predictions = predictions.argmax(axis=1)[0]
    return jsonify({'predictions ': str(predictions), 'Category ': target.get(predictions)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
