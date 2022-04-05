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

@app.route("/")
def list_data():
    return json.dumps(DATA)


@app.route('/data', methods=['POST', 'PUT'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)
