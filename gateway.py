import os
from flask import Flask, Response, jsonify, request
from flask_cors import CORS

import dataService

app = Flask(__name__)
CORS(app)

@app.route("/load-data", methods=['POST'])
def loadData():
    data = dataService.getData()
    response = {
        'file': 1,
        'message': 'File uploaded'
    }
    return jsonify(response)

@app.route("/get-data-list", methods=['GET'])
def getDataList():
    response = {
        'data': ['ListaMovimenti.csv', 'ListaMovimenti2.csv'],
        'message': 'ok'
    }
    return jsonify(response)

@app.route("/compute-data", methods=['GET'])
def getData():
    filename = request.args.get('filename')
    # 'ListaMovimenti.csv'
    data = dataService.getData(filename)
    response = {
        'generalValues': data[0],
        'weekAmounts': data[1],
        'yearIncomeOutcome': data[2],
        'salaries': data[3],
        'amazonExpenses': data[4],
        'outcomePerType': data[5]
    }
    return jsonify(response)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="127.0.0.1", port=5004, use_reloader=False)