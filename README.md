# baton

a simple coding exercise

initial requirements:

implement a web service with a REST API that has a single endpoint, /data. The endpoint should support a GET request to retrieve an array of data points (integers), as well as a POST request to add to the set of data points.

on debian 11:

```
sudo apt install python3-venv python3-virtualenv

python3 -m venv ./venv
source ./venv/bin/activate

pip install prometheus-flask-exporter

python3 ./flask-data-api.py

```

the last command above will serve flask app on http://0.0.0.0:5000/data


some sample curl calls (my hostname is `debian20220207aa`):
```
# get all rows
curl http://debian20220207aa:5000/data

# get one row
curl http://debian20220207aa:5000/data/d1

# post data to create a new row
curl -X POST -H "Content-type: application/json" -d "{\"data\" : [1, 23, \"purple\", 65] }" http://debian20220207aa:5000/data

# put new data on an existing row
curl -X PUT -H "Content-type: application/json" -d "{\"data\" : [1, 23, \"green\", 65] }" http://debian20220207aa:5000/data/d1

```
