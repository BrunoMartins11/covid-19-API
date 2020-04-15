from flask import Flask, request,send_from_directory
from flask_cors import CORS
import os

from Models.ArimaModel import ArimaModel
from Models.ExponentialSmootheningModel import ExponentialSmootheningModel
from Models.ProphetModel import ProphetModel
from Models.LstmModel import LstmModel
import pandas as pd

import dataset as datasetMaker


import sys


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
dir = os.path.dirname(__file__)

@app.route('/predictions', methods = ['GET'])
def country_csv_prediction():
    countries = request.args.get('country').split(",")
    time = request.args.get('days')
    field = request.args.get('field')

    data = datasetMaker.create_dataset(countries)
    dataset_to_use = data[ [field+x for x in countries] ]
    dataset_to_send = pd.DataFrame()

    model1 = ArimaModel()
    model2 = ExponentialSmootheningModel()
    model3 = ProphetModel()

    for i in countries:
        new_data1 = model1.predict_with_arima(dataset_to_use,i,field,int(time))
        new_data2 = model2.predict_with_exp(dataset_to_use,i,field,int(time))
        new_data3 = model3.predict_with_prophet(dataset_to_use,i,field,int(time))

        dataset_to_send = pd.concat([dataset_to_send,new_data1, new_data2, new_data3], axis=1, sort=False)

    datasetMaker.write_to_csv(dataset_to_send, "tmp")
    return send_from_directory(".","tmp.csv", as_attachment=True)


@app.route('/predictions_based_on', methods = ['GET'])
def country_based_on():
    base = request.args.get('base')
    target = request.args.get('target')
    field = request.args.get('field')

    data = datasetMaker.create_dataset([base,target])
    dataset = data[ [field+x for x in [base,target]] ]

    train_data = dataset[[field+base]]
    predict_data = dataset[[field+target]]

    lstm = LstmModel()
    lstm.train(train_data)
    fake_data = lstm.predict(predict_data)

    datasetMaker.write_to_csv(fake_data, "tmpOn")
    return send_from_directory(".","tmpOn.csv", as_attachment=True)

app.run(debug=True, port=5000)
