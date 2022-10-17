###主程式###

#linebot
from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

#字串處理
import configparser

#時間
from datetime import datetime
import datetime as dt

#陣列
import collections
from numpy import *
import numpy as np
from numpy.core.defchararray import isdigit 

#Log
import logging
Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "LineageM/LineageM_other.log",
                    format = Log_Format, 
                    level = logging.INFO)
handler = logging.FileHandler('LineageM/LineageM_other.log',encoding='utf-8')

#本機資源
import os
from CheckBossList import BossListCheck
from CheckSilence import SilenceListCheck
from CheckWeekOpen import WeekOpenCheck
from CheckPassList import PassListCheck
from RecordList import RecodeListCheck
import MemberList
from BossRequest import StringSet
from MemberJoin import MemberSet
from CheckKeyWordList import KeywordListCheck

import random

import requests

#是否暫停回應
silenceTag = np.load('LineageM/Silence.npy')

app = Flask(__name__)

# LINE 聊天機器人的基本資料
channel_access_token = 'IuZDQ7Afa71I4p3SIpKaQB/rgompmOTciSqBYAIRHURxkZJ5jNzJ3rnpM23goDCS0LHYrZL9mxob5sqKiJrg9dDzejUyVdZYKojwnUhnwWEm3yTWzmpoNyDOy1X8YQmqYrJibqlMYMFKnYYTAiVDTQdB04t89/1O/w1cDnyilFU='
channel_secret =  '0ebf68963810f38454c8c89f9441dad9'

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

#允許回復對象清單
'''
Cffb6b6d9803657ef096cdbb3286e148d:打爆
C170c945b6592d42bb53aac14747edf12:水蛇王表
Cbd816f538c007ac5fed24fada5eb1d4b:水蛇小王表
Ubd9ed8a37a5a51fe3da408c9359883a9:波多野小教室
C9b459635d139461ecbce3a368ac21542:布魯迪卡小王表
C036ed4d1b17ac0df40fe42e776a4f479:半人馬小王表
C6a2a470757e902298da9e4d03eeadca7:布魯迪卡小王表对照表
Cd4de4138f400161d73d3615d9b7b76a3:海胆(卡司特调整为2.5H/狼調整為4H)
C3a8a414b547f216de7f4a0e15cf2e4f4:海膽2號(卡司特调整为2.5H/狼調整為4H)
'''
ConfirmReply = [
    'Ubd9ed8a37a5a51fe3da408c9359883a9',
    'C9b459635d139461ecbce3a368ac21542',
    'C036ed4d1b17ac0df40fe42e776a4f479',
    'C6a2a470757e902298da9e4d03eeadca7',
    'Cd4de4138f400161d73d3615d9b7b76a3',
    'C3a8a414b547f216de7f4a0e15cf2e4f4'
    ]
MemberReply = ['Ubd9ed8a37a5a51fe3da408c9359883a9']

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'

#接收訊息及判斷做回應
@handler.add(MessageEvent, message=TextMessage)
def prettyEcho(event):
    
    #接收訊息
    askString = event.message.text

    checkid = ''
    if event.source.type == 'group':
        checkid = event.source.group_id
        headers = {"content-type": "application/json; charset=UTF-8",'Authorization':'Bearer {}'.format(channel_access_token)}
        url = 'https://api.line.me/v2/bot/group/' + event.source.group_id + '/member/' + event.source.user_id
        response = requests.get(url, headers=headers)
        response = response.json()
        userName = response['displayName']
    elif event.source.type == 'user':
        checkid = event.source.user_id
        try:
            userName = line_bot_api.get_profile(event.source.user_id).display_name
        except:
            userName = ''

    if checkid in ConfirmReply:
        BossListCheck(checkid)
        SilenceListCheck(checkid)
        WeekOpenCheck(checkid)
        PassListCheck(checkid)
        RecodeListCheck(checkid)
        KeywordListCheck(checkid)

    #StrAskType = askString.split(" ", 3)[0]
    #要先內宣告一次再給指定不然會報錯
    """ sendString = ''
    if StrAskType in ('新增成員','修改成員','刪除成員','成員職業','成員血盟','血盟','血盟指令','成員Line','成員賴','成員','職業','職業對照'):
        sendString = MemberSet(askString,userName)
    else:
        sendString = StringSet(askString,userName,checkid)
    #實際回應
    if StrAskType == '指令':
        sendString = '輸入"王表指令"：查詢王表相關操作\n'
        if checkid in MemberReply:
            sendString = sendString + '輸入"血盟指令"：查詢血盟成員相關操作\n'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=sendString)
        )
    elif len(sendString) > 0 and checkid in ConfirmReply:
        if np.load('LineageM/Silence_' + checkid + '.npy') == 1:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=sendString)
            ) """
    sendString = StringSet(askString,userName,checkid)
    if len(sendString) > 0 and checkid in ConfirmReply:
        if np.load('LineageM/Silence_' + checkid + '.npy') == 1:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=sendString)
            )

if __name__ == "__main__":
    app.run()