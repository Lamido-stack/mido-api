import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    data_set = {"slackUsername": "Lamido", "backend": True, "age": 22, "bio": "Im a tech enthusiast on a journey of self realisation" }
    arg = request.args['arg1']
    return data_set