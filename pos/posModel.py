import logging
# 藍圖
from flask import Blueprint

pos_model = Blueprint('pos', __name__)

@pos_model.route('/', methods=["GET"])
# 簡單做實作Get就好
def index():
    return "abc"
