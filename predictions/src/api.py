from flask import Flask, request,send_from_directory
import os

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
