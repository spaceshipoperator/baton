import json
import time
import random

from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

DATA = {
    "d1": [1, 2, 34, "orange"],
    "d2": [2, 33, 4]
    }


@app.route("/data")
def list_data():
    return json.dumps(DATA)


@app.route('/data/<data_id>', methods=['GET', 'PUT'])
def get_data(data_id):
    content_type = request.headers.get('Content-Type')
    if (request.method == 'PUT'):
        if (content_type == 'application/json'):
            print("append new data to row: {}".format(data_id))
            d = DATA[data_id]
            j = request.json
            DATA[data_id] = [ *d, *j["data"] ]
            return json.dumps(DATA[data_id])
        else:
            return 'Content-Type not supported!'
    else:
        print("get the data row: {}".format(data_id))
        return json.dumps(DATA[data_id])


@app.route('/data', methods=['POST'])
def process_data():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        print("add a new row with id: d{}".format(len(DATA)))
        j = request.json
        return j
    else:
        return 'Content-Type not supported!'


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)
