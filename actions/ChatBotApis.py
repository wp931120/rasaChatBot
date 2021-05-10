# 访问图灵机器人openapi
# -*- coding: utf-8 -*-
"""
    ChatApis.py
    ~~~~~~~~~
    图灵机器人(公司)闲聊系统API对接
    免费版只限每天调用100次，需联外网
    :date: 2020-02-10 15:56:00
    :author: by jiangdg
"""
import requests
import json


def get_response(msg):
    """
        访问图灵机器人openApi
        :param msg 用户输入的文本消息
        :return string or None
    """
    apiurl = "http://openapi.tuling123.com/openapi/api/v2"
    # 构造请求参数实体
    params = {"reqType": 0,
              "perception": {
                  "inputText": {
                      "text": msg
                  }
              },
              "userInfo": {
                  "apiKey": "7585f52002e841ed8ad97f6a4484693e",
                  "userId": "439608"
              }}
    # 将表单转换为json格式
    content = json.dumps(params)

    # 发起post请求
    r = requests.post(url=apiurl, data=content, verify=False).json()
    print("r = " + str(r))
    message = r['results'][0]['values']['text']
    return message


if __name__ == '__main__':
    print(get_response("天气机器人"))