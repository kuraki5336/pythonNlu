def baseCard():
    return {
        "platform": "ACTIONS_ON_GOOGLE",
        "basicCard": {
            "title": "龍妹",
            "subtitle": "管理員",
            "formattedText": "你好，歡迎使用",
            "image": {
                "imageUri": "https://i.imgur.com/5VZjxgL.jpg",
                "accessibilityText": "666"
            },
            "buttons": [
                {
                    "title": "圖片鏈結",
                    "openUriAction": {
                        "uri": "https://i.imgur.com/5VZjxgL.jpg"
                    }
                }
            ]
        }
    }

# 列表卡
def listCard():
    return {
        "platform": "ACTIONS_ON_GOOGLE",
        "listSelect": {
            "title": "01",
            "items": [
                {
                    "info": {
                        "key": "01"
                    },
                    "title": "測試1",
                    "image": {}
                },
                {
                    "info": {
                        "key": "02"
                    },
                    "title": "測試2",
                    "image": {}
                }
            ]
        }
    }

# 標籤模式
def tagCard():
    return {
        "platform": "ACTIONS_ON_GOOGLE",
        "suggestions": {
            "suggestions": [
                    {
                        "title": "666"
                    },
                {
                        "title": "7777"
                }
            ]
        }
    },
    {
        "text": {
            "text": [
                ""
            ]
        }
    }


# 輪播卡
def rollCard():
    return {
        "platform": "ACTIONS_ON_GOOGLE",
        "carouselSelect": {
            "items": [
                {
                    "info": {
                        "key": "01"
                    },
                    "title": "01",
                    "description": "01",
                    "image": {
                        "imageUri": "https://i.imgur.com/5VZjxgL.jpg",
                        "accessibilityText": "111"
                    }
                },
                {
                    "info": {
                        "key": "02"
                    },
                    "title": "02",
                    "description": "02",
                    "image": {
                        "imageUri": "https://i.imgur.com/QWTvQWu.jpg",
                        "accessibilityText": "222"
                    }
                }
            ]
        }
    }

# 標籤超連結


def tagurlCard():
    return {
        "platform": "ACTIONS_ON_GOOGLE",
        "linkOutSuggestion": {
            "destinationName": "超連結哦",
            "uri": "https://imgur.com/QWTvQWu"
        }
    }


#  圖表
def tableCard():
    return {
        "platform": "ACTIONS_ON_GOOGLE",
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "54321"
                }
            ]
        }
    },
    {
        "platform": "ACTIONS_ON_GOOGLE",
        "tableCard": {
            "title": "浣熊",
            "image": {
                "imageUri": "https://i.imgur.com/QWTvQWu.jpg"
            },
            "columnProperties": [
                {
                    "horizontalAlignment": "LEADING"
                },
                {
                    "horizontalAlignment": "CENTER"
                },
                {
                    "horizontalAlignment": "TRAILING"
                }
            ],
            "rows": [
                {
                    "cells": [
                        {
                            "text": "001"
                        },
                        {
                            "text": "002"
                        },
                        {
                            "text": "003"
                        }
                    ]
                },
                {
                    "cells": [
                        {
                            "text": "004"
                        },
                        {
                            "text": "005"
                        },
                        {
                            "text": "006"
                        }
                    ]
                },
                {
                    "cells": [
                        {
                            "text": "007"
                        },
                        {
                            "text": "008"
                        },
                        {
                            "text": "009"
                        }
                    ]
                }
            ]
        }
    }


def mediaCard():
    return {
        "platform": "ACTIONS_ON_GOOGLE",
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "要說句話哦"
                }
            ]
        }
    },
    {
        "platform": "ACTIONS_ON_GOOGLE",
        "mediaContent": {
            "mediaType": "AUDIO",
            "mediaObjects": [
                {
                    "name": "測試影片",
                    "description": "......",
                    "largeImage": {
                        "imageUri": "https://imgur.com/QWTvQWu",
                        "accessibilityText": "666"
                    },
                    "contentUrl": "https://www.youtube.com/watch?v=amLM8pxaSx0"
                }
            ]
        }
    },
    {
        "platform": "ACTIONS_ON_GOOGLE",
        "suggestions": {
            "suggestions": [
                {
                    "title": "666"
                }
            ]
        }
    }
