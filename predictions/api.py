from flask import Flask, request,send_from_directory
import os

from Models.ArimaModel import ArimaModel
from Models.ExponentialSmootheningModel import ExponentialSmootheningModel
from Models.ProphetModel import ProphetModel

app = Flask(__name__)

dir = os.path.dirname(__file__)

@app.route('/country.csv', methods = ['GET'])
def country_csv():
    if (request.data):
        req_data = request.get_json()
        countries = req_data.keys()
        print(countries)
        return send_from_directory(dir, 'ola.csv', as_attachment=True)

app.run(debug=True, port=5000)
