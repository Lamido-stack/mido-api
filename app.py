import flask
from flask import request
import json

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    data_set = {'slackUsername': 'Lamido', 'backend': True, 'age': 22, 'bio': 'Im a tech enthusiast on a journey of self realisation'}
    json_dump = json.dumps(data_set)
    return json_dump