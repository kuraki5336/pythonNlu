import logging
# 藍圖
from flask import Blueprint, jsonify, request
# 類似interface必需的宣告
from flask_restful import reqparse
# 注意是requests 有s
import requests
import json

# 標準卡
from nlu.nluBasecard import baseCard, listCard, tagCard, rollCard, tagurlCard, tableCard, mediaCard

nlu_model = Blueprint('nlu', __name__)

# request.form['datetime'] 這種是form的接法
# request.json RAW寫法
# logging.warning(request.form)  寫LOG方法
@nlu_model.route('/', methods=["POST"])
# 簡單做實作Get就好
def index():
    # abc = baseCard()
    url_API = 'http://203.69.87.154:18115/users/000000000000000000000000/apps/c9c91aa42a6ae579dab8.ad98a27d1ea6/api/?token=atzbwz165bRYsdJIyw'

    token = 'xolWmySCh74pySt1HYsQ2skZEoj8zebdgqbxKFIqP3h'

    # 取得GCP給過的值
    content = request.json
    

    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "message": {
            "type": 1,
            "text": content["queryResult"]["queryText"]
        },
        "sessionId": content["session"]
    }

    try:
        r = requests.post(url_API, headers=headers, data=json.dumps(payload))
        # 替換文字
        repjson = json.loads(r.text)
        
        for item in repjson['messages']:
            if item["type"] == 1:
                # 完成回傳
                # data = json.dumps(baseCard())
                data = baseCard()
                data1= listCard()
                # tagCard, rollCard, 
                # tagurlCard, 
                # tableCard, 
                # mediaCard
                logging.warning(data1)
                rep = {
                    'fulfillmentMessages': [
                        {
                            "platform": "ACTIONS_ON_GOOGLE",
                            "simpleResponses": {
                                "simpleResponses": [
                                    {
                                        "textToSpeech": item["text"]
                                    }
                                ]
                            }
                        },
                        data,
                        data1
                    ]
                }
        logging.warning(rep)
        return rep

    except requests.exceptions.RequestException as e:
        logging.warning(e)
