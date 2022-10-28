import flask
from flask import *
import json

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Home'


@app.route("/mido")
def test():
    data_set = {'slackUsername': 'Lamido', 'backend': True, 'age': 22, 'bio': 'Im a tech enthusiast on a journey of self realisation'}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__=="__main__":
    app.run() 