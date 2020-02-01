# This is the Flask server
from flask import Flask, request, jsonify
#from parse_water_footprint import *
import requests
import json
from parse_data_feed import *

app = Flask(__name__)

parser = CSVParser();

@app.rout('/')
def h():
    return "H"

@app.route('/welcome')
def hello():
    return 'hello'

@app.route('/layout_info')
def get_info():
    return parser.get_layout("Layout1")

if __name__ == '__main__':
	app.run(debug=True, port=5000)
