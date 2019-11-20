from flask import Flask
import sys
import logging
import ssl
import json
from nlu.nluModel import nlu_model
from pos.posModel import pos_model


app = Flask(__name__)
# Debug等級
# logging.basicConfig(level=logging.DEBUG)
# 註冊藍本
app.register_blueprint(nlu_model, url_prefix='/nlu')
app.register_blueprint(pos_model, url_prefix='/pos')


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/home')
def index():
    return ""


# 本機用
app.run(host="0.0.0.0", debug=True)
# app.run(debug=True)
