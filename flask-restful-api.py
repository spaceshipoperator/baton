#!/bin/python3

# Note: bmuckian@gmail.com
# (shamelessly) borrowed from / based upon example provided within:
# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# refactored and repurposed

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

DATA = {
        "data1": { "items": [1, 2, 3] },
        "data2": { "items": [4, 5, 6] }, 
        "data3": { "items": [34, 25, 96, "orange"] },
}

def abort_if_data_doesnt_exist(data_id):
    if data_id not in DATA:
        abort(404, message="Data {} doesn't exist".format(data_id))

parser = reqparse.RequestParser()
parser.add_argument('items')


# Data
# shows data row items and lets you delete, modify, add items
class Data(Resource):
    def get(self, data_id):
        abort_if_data_doesnt_exist(data_id)
        return DATA[data_id]

    def delete(self, data_id):
        abort_if_data_doesnt_exist(data_id)
        del DATA[data_id]
        return '', 204

    def put(self, data_id):
        args = parser.parse_args()
        items = {'items': args['items']}
        DATA[data_id] = items
        return items, 201


# DataList
# shows a list of all data rows, and POST to add new items
class DataList(Resource):
    def get(self):
        return DATA

    def post(self):
        args = parser.parse_args()
        data_id = int(max(DATA.keys()).lstrip('data')) + 1
        data_id = 'data%i' % data_id
        DATA[data_id] = {'items': args['items']}
        return DATA[data_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(DataList, '/data')
api.add_resource(Data, '/data/<data_id>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
