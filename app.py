import flask
from flask import *
import json

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    data = json.load(open('data.json'))
    return data