###主程式###

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
#import logging
#Log_Format = "%(levelname)s %(asctime)s - %(message)s"

#logging.basicConfig(filename = "D:/LineageM/LineageM_other.log",
#                    format = Log_Format, 
#                    level = logging.INFO)
#handler = logging.FileHandler('D:/LineageM/LineageM_other.log',encoding='utf-8')

#本機資源
import os
from CheckBossList import BossListCheck
from CheckSilence import SilenceListCheck
from CheckWeekOpen import WeekOpenCheck
from CheckPassList import PassListCheck
from RecordList import RecodeListCheck
#import MemberList
from BossRequest import StringSet
#from MemberJoin import MemberSet
from CheckKeyWordList import KeywordListCheck

import random

import requests

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
    'C3a8a414b547f216de7f4a0e15cf2e4f4'
    ]
#MemberReply = ['Ubd9ed8a37a5a51fe3da408c9359883a9']


#接收訊息
askString = "出"

checkid = 'C9b459635d139461ecbce3a368ac21542'

userName = ""

'''if checkid in ConfirmReply:
    BossListCheck(checkid)
    
    SilenceListCheck(checkid)
    WeekOpenCheck(checkid)
    PassListCheck(checkid)
    RecodeListCheck(checkid)
    KeywordListCheck(checkid)

    sendString = StringSet(askString,userName,checkid)
    print(sendString)
'''
Boss_List = np.load('D:/LineageM/Boss_List_' + checkid + '.npy',allow_pickle=True)
Pass_List = np.load('D:/LineageM/Pass_List_' + checkid + '.npy',allow_pickle=True)
KeywordList = np.load('D:/LineageM/KeywordList_' + checkid + '.npy',allow_pickle=True)
print(KeywordList)