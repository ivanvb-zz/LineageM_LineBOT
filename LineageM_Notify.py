import requests

#字串處理
import configparser

#時間
from datetime import datetime
import datetime as dt
import time

#陣列
import collections
from numpy import *
import numpy as np
from numpy.core.defchararray import isdigit 

import os
from CheckBossList import BossListCheck
from CheckSilence import SilenceListCheck
from CheckWeekOpen import WeekOpenCheck
from CheckPassList import PassListCheck
from RecordList import RecodeListCheck
from BossRequest import StringSet

#時間
from datetime import datetime
import datetime as dt


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

GroupList = [
    ['C9b459635d139461ecbce3a368ac21542','hb8E3jR028lvDbENeSkUJiWh5CzjLfOXTo1OMwUz4YX',]
    #['C170c945b6592d42bb53aac14747edf12','PLoSN5vQSV2MPOtpCVXm4Yi0XKnlR3kfis6Lmi4hDxs']
    #,['C170c945b6592d42bb53aac14747edf12','ph6cGqz24KG4D9ynwh9OzDR2aSavogRcN4UH8JRqaof']
    ]

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

loop = 0
while loop >= 0:
    current_date = datetime.now()

    for i in range(0,len(GroupList)):
        checkid = GroupList[i][0]
        # 修改為你的權杖內容
        token = GroupList[i][1]
        sendStringTemp = '即將重生：\n'
        GiantStrTemp = '奇岩地監：\n'
        SplitLine = '{:-^25s}'.format('') + '\n'

        Boss_List = np.load('LineageM/Boss_List_' + checkid + '.npy')
        OpenDatetime = np.load('LineageM/WeekOpen_' + checkid + '.npy',allow_pickle=True)
        Pass_List = np.load('LineageM/Pass_List_' + checkid + '.npy',allow_pickle=True)
        GiantBoss_List = np.load('LineageM/GiantBoss_List.npy',allow_pickle=True)
        Record = np.load('LineageM/RecordList_' + checkid + '.npy',allow_pickle=True)

        for i in range(0,len(Boss_List)):
            if Boss_List[i][1] not in ('浮士德','巴風特','魔法師'):
                #判斷時間及計算下次重生時間
                if len(Boss_List[i][3]) > 0:
                    while current_date > datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S'):
                        Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Boss_List[i][2]))
                        Boss_List[i][4] = int(Boss_List[i][4]) + 1

                #重新存檔
                np.save('LineageM/Boss_List_' + checkid, Boss_List)
                
        Boss_List = sorted(Boss_List,key=lambda x:x[3])

        for i in range(0,len(Boss_List)):
            if len(Boss_List[i][3]) > 0:
                if datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') > current_date \
                    and datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') < current_date + dt.timedelta(seconds=3600):
                    if Boss_List[i][1] not in ('浮士德','巴風特','魔法師'):

                        #是否回傳備註
                        if len(str(Boss_List[i][5])) >= 0:
                            memostr = str(Boss_List[i][5])
                        else:
                            memostr = ''

                        if len(Boss_List[i][4]) > 0 and int(Boss_List[i][4]) > 0 and Boss_List[i][1] not in ('魔法師'):
                            passstr = '過[' + Boss_List[i][4] + '] '
                        else:
                            passstr = ''

                        if len(Boss_List[i][3]) > 0:
                            #Boss_name = '{name:<{len}}\t'.format(name=str(Boss_List[i][1]),len=8-len(str(Boss_List[i][1]).encode('GBK'))+len(str(Boss_List[i][1]).encode('GBK')))
                            Boss_name = str(Boss_List[i][1]).ljust(8-len(str(Boss_List[i][1]).encode('GBK'))+len(str(Boss_List[i][1])))
                            sendStringTemp = sendStringTemp + str(Boss_List[i][3])[11:19] + ' '
                            sendStringTemp = sendStringTemp + Boss_name
                            sendStringTemp = sendStringTemp + passstr
                            sendStringTemp = sendStringTemp + memostr + '\n'

        for i in range(0,len(GiantBoss_List)):
            #判斷時間及計算下次重生時間
            if len(GiantBoss_List[i][3]) > 0:
                while current_date >= datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S'):
                    GiantBoss_List[i][3] = datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(GiantBoss_List[i][2]))
        #重新存檔
        GiantBoss_List = sorted(GiantBoss_List,key=lambda x:x[3])
        np.save('LineageM/GiantBoss_List', GiantBoss_List)
        
        if current_date.isoweekday() in (1,2,3,4,5):
            for i in range(0,len(GiantBoss_List)):
                if current_date >= datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=3600) \
                    and current_date < datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=3600):
                    if len(GiantBoss_List[i][3]) > 0 \
                        and (datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=60)).isoweekday() in (1,2,3,4,5):
                        #Boss_name = '{name:<{len}}\t'.format(name=str(Pass_List[i][1]),len=8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1]).encode('GBK')))
                        Boss_name = str(GiantBoss_List[i][1]).ljust(8-len(str(GiantBoss_List[i][1]).encode('GBK'))+len(str(GiantBoss_List[i][1])))
                        GiantStrTemp = GiantStrTemp + str(GiantBoss_List[i][3])[11:19] + ' ' #時間
                        GiantStrTemp = GiantStrTemp + Boss_name + '\n'                #王名

        # 修改為你要傳送的訊息內容
        message = '\n' + GiantStrTemp + SplitLine + sendStringTemp
        #message = '\n' + sendStringTemp
        print(datetime.now())
        print(message)
        lineNotifyMessage(token, message)

    time.sleep(sleeptime(0,30,0))