from flask import Flask, request

app = Flask(__name__)

@app.route('/csv', methods = ['GET'])
def country_csv():
    req_data = request.get_json()
    countries = req_data.keys()
    print(countries)
    return "Json received"

app.run(debug=True, port=5000)
