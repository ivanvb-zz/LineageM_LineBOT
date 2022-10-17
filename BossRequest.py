###王表主功能###

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

#本機資源
import os

def StringSet(askString,userName,checkid):
    #王表
    #[0]:代碼
    #[1]:名稱
    #[2]:重生時間(分)
    #[3]:最近一次回報
    #[4]:錯過次數
    #[5]:備註

    if checkid == 'Cffb6b6d9803657ef096cdbb3286e148d':
        pass

    if checkid == 'Ubd9ed8a37a5a51fe3da408c9359883a9':
        checkid = 'C9b459635d139461ecbce3a368ac21542'

    setrecord = 1   #是否紀錄 1:是,0:否
    strexists = 1   #關鍵字判斷 1:存在,0:不存在
    current_date = datetime.now()
    sendStringTemp = ''
    PassStrTemp = ''
    SplitLine = ''
    GiantStrTemp = ''
    StandardStrTemp = ''

    Boss_List = np.load('LineageM/Boss_List_' + checkid + '.npy',allow_pickle=True)
    OpenDatetime = np.load('LineageM/WeekOpen_' + checkid + '.npy',allow_pickle=True)
    Pass_List = np.load('LineageM/Pass_List_' + checkid + '.npy')
    GiantBoss_List = np.load('LineageM/GiantBoss_List.npy')
    StandardBoss_List = np.load('LineageM/StandardBoss_List.npy')
    Record = np.load('LineageM/RecordList_' + checkid + '.npy',allow_pickle=True)
    KeyWordList = np.load('LineageM/KeywordList_' + checkid + '.npy',allow_pickle=True)

    #把出王時間型別改成datetime
    for i in range(0,len(Boss_List)):
        #if Boss_List[i][1] not in ('惡魔監視者','曼波兔王','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
        if Boss_List[i][1] not in ('浮士德','巴風特','魔法師') and len(Boss_List[i][3]) > 0:
            Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S')
        #else:
            #Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d')

    #指令
    if askString == '王表指令':
        sendStringTemp = ('王表指令說明(@表示空格)：\n')
        sendStringTemp = sendStringTemp + '一般查詢\n'
        sendStringTemp = sendStringTemp + '重生　　：王重生時間\n'
        sendStringTemp = sendStringTemp + '出　　　：出王時間表\n'
        sendStringTemp = sendStringTemp + '特/特出  ：特殊王時間表\n'
        sendStringTemp = sendStringTemp + '過　　　：前次錯過時間表\n'
        sendStringTemp = sendStringTemp + '開機　　：本週開機時間\n'
        sendStringTemp = sendStringTemp + '30　　　：王出30分內未打\n'
        sendStringTemp = sendStringTemp + '紀錄　　：最近6筆紀錄\n'
        sendStringTemp = sendStringTemp + 'key　　：野王代碼\n'
        sendStringTemp = sendStringTemp + 'key@關鍵字：查詢包含關鍵字的野王\n'
        sendStringTemp = sendStringTemp + '\n設定\n'
        sendStringTemp = sendStringTemp + 'resetdata    ：王表重置\n'
        sendStringTemp = sendStringTemp + '時間@開　　：重置開機時間\n'
        sendStringTemp = sendStringTemp + '時間@關鍵字：設定王死時間\n'
        sendStringTemp = sendStringTemp + '+/666@關鍵字：使用+或666則設定當下系統時間為王死時間\n'
        sendStringTemp = sendStringTemp + '如需加備註請在關鍵字後面空一格後再加\n'
        sendStringTemp = sendStringTemp + '時間請輸入四碼(時+分)或六碼數字(時分秒)\n'
        sendStringTemp = sendStringTemp + 'add@王名@關鍵字：設定野王關鍵字(add 死騎 螢光棒→新增死騎關鍵字"螢光棒")\n'
        sendStringTemp = sendStringTemp + 'del@王名@關鍵字：刪除野王關鍵字(del 死騎 螢光棒→刪除死騎關鍵字"螢光棒")\n'
        #sendStringTemp = sendStringTemp + '\n回應開關\n'
        #sendStringTemp = sendStringTemp + '老布B嘴：關閉回應(仍可更新王表但不回傳訊息)\n'
        #sendStringTemp = sendStringTemp + '老布吃餐包：開啟回應(重新開始正常回傳訊息))\n'
        
        setrecord = 0
    #resetdata
    elif askString == 'resetdata':
        OpenDatetime = ''
        for i in range(0,len(Boss_List)):
            Boss_List[i][3] = ''
            Boss_List[i][4] = ''
            Boss_List[i][5] = ''
        for i in range(0,len(Pass_List)):
            Pass_List[i][3] = ''
            Pass_List[i][4] = ''
            Pass_List[i][5] = ''
        for i in range(0,len(Record)):
            for j in range(2,8):
                Record[i][j] = ''
        sendStringTemp = '王表時間已重置完成'
        #重新存檔
        np.save('LineageM/Boss_List_' + checkid, Boss_List)
        np.save('LineageM/WeekOpen_' + checkid, OpenDatetime)
        np.save('LineageM/Pass_List_' + checkid, Pass_List)
        np.save('LineageM/RecordList_' + checkid, Record)
        setrecord = 0
    #本週開機時間
    elif askString == '開機':
        sendStringTemp = '本週開機時間為 ' + str(OpenDatetime)
        setrecord = 0
     #本週開機時間
    elif askString == '30':
        PassStrTemp = '30分內未打：\n'
        for i in range(0,len(Pass_List)):
            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
            if Pass_List[i][1] not in ('浮士德','巴風特','魔法師') \
                and current_date >= datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') \
                and current_date < datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):

                #是否回傳備註
                if len(str(Pass_List[i][5])) >= 0:
                    memostr = str(Pass_List[i][5])
                else:
                    memostr = ''

                if len(Pass_List[i][4]) > 0 and int(Pass_List[i][4]) > 0 and Pass_List[i][1] not in ('魔法師'):
                    passstr = '過[' + Pass_List[i][4] + '] '
                else:
                    passstr = ''

                if len(Pass_List[i][3]) > 0:
                    PassStrTemp = PassStrTemp + str(Pass_List[i][3])[11:19] + ' ' #時間
                    PassStrTemp = PassStrTemp + str(Pass_List[i][1]) + ' '        #王名
                    PassStrTemp = PassStrTemp + passstr                           #是否錯過
                    PassStrTemp = PassStrTemp + memostr + '\n'                    #備註
        setrecord = 0
    #老布B嘴
    elif askString == '老布B嘴':
        silenceTag = 0
        np.save('LineageM/Silence_' + checkid, silenceTag)
        sendStringTemp = ''
        setrecord = 0
    #老布吃餐包
    elif askString == '老布吃餐包':
        silenceTag = 1
        np.save('LineageM/Silence_' + checkid, silenceTag)

        sendStringTemp = '出王時間表：\n'
        PassStrTemp = '30分內未打：\n'
        GiantStrTemp = '奇岩地監：\n'
        StandardStrTemp = '固定王：\n'
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

        for i in range(0,len(Pass_List)):
            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
            if Pass_List[i][1] not in ('浮士德','巴風特','魔法師') and len(Pass_List[i][3]) > 0:
                #是否回傳備註
                if len(str(Pass_List[i][5])) >= 0:
                    memostr = str(Pass_List[i][5])
                else:
                    memostr = ''

                #判斷時間及計算下次重生時間
                while current_date > datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):
                    Pass_List[i][3] = datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Pass_List[i][2]))
                    Pass_List[i][4] = int(Pass_List[i][4]) + 1

                if int(Pass_List[i][4]) > 0 and Pass_List[i][1] not in ('魔法師'):
                    passstr = '過[' + Pass_List[i][4] + '] '
                else:
                    passstr = ''

        #重新存檔
        np.save('LineageM/Pass_List_' + checkid, Pass_List)

        Pass_List = sorted(Pass_List,key=lambda x:x[3])

        for i in range(0,len(Boss_List)):
            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
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
                    sendStringTemp = sendStringTemp + str(Boss_List[i][3])[11:19] + ' ' #時間
                    sendStringTemp = sendStringTemp + Boss_name                         #王名
                    sendStringTemp = sendStringTemp + passstr                           #是否錯過
                    sendStringTemp = sendStringTemp + memostr + '\n'                    #備註

        for i in range(0,len(Pass_List)):
            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
            if Pass_List[i][1] not in ('浮士德','巴風特','魔法師') and len(Pass_List[i][3]) > 0 \
                and current_date >= datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') \
                and current_date < datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):

                #是否回傳備註
                if len(str(Pass_List[i][5])) >= 0:
                    memostr = str(Pass_List[i][5])
                else:
                    memostr = ''

                if len(Pass_List[i][4]) > 0 and int(Pass_List[i][4]) > 0 and Pass_List[i][1] not in ('魔法師'):
                    passstr = '過[' + Pass_List[i][4] + '] '
                else:
                    passstr = ''

                if len(Pass_List[i][3]) > 0:
                    #Boss_name = '{name:<{len}}\t'.format(name=str(Pass_List[i][1]),len=8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1]).encode('GBK')))
                    Boss_name = str(Pass_List[i][1]).ljust(8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1])))
                    PassStrTemp = PassStrTemp + str(Pass_List[i][3])[11:19] + ' ' #時間
                    PassStrTemp = PassStrTemp + Boss_name                         #王名
                    PassStrTemp = PassStrTemp + passstr                           #是否錯過
                    PassStrTemp = PassStrTemp + memostr + '\n'                    #備註
        SplitLine = '{:-^25s}'.format('') + '\n'

        for i in range(0,len(GiantBoss_List)):
            #判斷時間及計算下次重生時間
            if len(GiantBoss_List[i][3]) > 0:
                while current_date > datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=600):
                    GiantBoss_List[i][3] = datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(GiantBoss_List[i][2]))

        #重新存檔
        GiantBoss_List = sorted(GiantBoss_List,key=lambda x:x[3])
        np.save('LineageM/GiantBoss_List', GiantBoss_List)

        if current_date.isoweekday() in (1,2,3,4,5):
            for i in range(0,len(GiantBoss_List)):
                if current_date >= datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=3600) \
                    and current_date < datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):

                    if len(GiantBoss_List[i][3]) > 0 \
                        and (datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=60)).isoweekday() in (1,2,3,4,5):
                        #Boss_name = '{name:<{len}}\t'.format(name=str(Pass_List[i][1]),len=8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1]).encode('GBK')))
                        Boss_name = str(GiantBoss_List[i][1]).ljust(8-len(str(GiantBoss_List[i][1]).encode('GBK'))+len(str(GiantBoss_List[i][1])))
                        GiantStrTemp = GiantStrTemp + str(GiantBoss_List[i][3])[11:19] + ' ' #時間
                        GiantStrTemp = GiantStrTemp + Boss_name + '\n'                #王名
        else:
            GiantStrTemp = GiantStrTemp + '本日公休\n'

        for i in range(0,len(StandardBoss_List)):
            #判斷時間及計算下次重生時間
            if len(StandardBoss_List[i][3]) > 0:
                while current_date > datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=600):
                    StandardBoss_List[i][3] = datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(StandardBoss_List[i][2]))

        #重新存檔
        StandardBoss_List = sorted(StandardBoss_List,key=lambda x:x[3])
        np.save('LineageM/StandardBoss_List', StandardBoss_List)

        for i in range(0,len(StandardBoss_List)):
            if current_date >= datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=3600) \
                and current_date < datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):

                if len(StandardBoss_List[i][3]) > 0:
                    Boss_name = str(StandardBoss_List[i][1]).ljust(8-len(str(StandardBoss_List[i][1]).encode('GBK'))+len(str(StandardBoss_List[i][1])))
                    StandardStrTemp = StandardStrTemp + str(StandardBoss_List[i][3])[11:19] + ' ' #時間
                    StandardStrTemp = StandardStrTemp + Boss_name + '\n'                #王名

        setrecord = 0
    #重生查詢
    elif askString == '重生':
        sendStringTemp = ('王重生時間：\n')
        for i in range(0,len(Boss_List)):
            sendStringTemp = sendStringTemp + str(Boss_List[i][1]) + ' '  + str(int(Boss_List[i][2])//3600) + '小時'
            sendStringTemp = sendStringTemp + str(int(Boss_List[i][2])%3600//60) + '分'
            sendStringTemp = sendStringTemp  + str(int(Boss_List[i][2])%3600%60) + '秒\n'
            
        setrecord = 0
    #出王查詢
    elif askString == '出':
        sendStringTemp = '出王時間表：\n'
        PassStrTemp = '30分內未打：\n'
        GiantStrTemp = '奇岩地監：\n'
        StandardStrTemp = '固定王：\n'

        for i in range(0,len(Boss_List)):
            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
            if Boss_List[i][1] not in ('浮士德','巴風特','魔法師'):
                #判斷時間及計算下次重生時間
                if len(Boss_List[i][3]) > 0:
                    while current_date > datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S'):
                        Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Boss_List[i][2]))
                        Boss_List[i][4] = int(Boss_List[i][4]) + 1

                #重新存檔
                np.save('LineageM/Boss_List_' + checkid, Boss_List)
                
        Boss_List = sorted(Boss_List,key=lambda x:x[3])

        for i in range(0,len(Pass_List)):
            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
            if Pass_List[i][1] not in ('浮士德','巴風特','魔法師') and len(Pass_List[i][3]) > 0:
                #是否回傳備註
                if len(str(Pass_List[i][5])) >= 0:
                    memostr = str(Pass_List[i][5])
                else:
                    memostr = ''

                #判斷時間及計算下次重生時間
                while current_date > datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):
                    Pass_List[i][3] = datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Pass_List[i][2]))
                    Pass_List[i][4] = int(Pass_List[i][4]) + 1

                if int(Pass_List[i][4]) > 0 and Pass_List[i][1] not in ('魔法師'):
                    passstr = '過[' + Pass_List[i][4] + '] '
                else:
                    passstr = ''

        #重新存檔
        np.save('LineageM/Pass_List_' + checkid, Pass_List)

        Pass_List = sorted(Pass_List,key=lambda x:x[3])

        for i in range(0,len(Boss_List)):
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

        for i in range(0,len(Pass_List)):
            if Pass_List[i][1] not in ('浮士德','巴風特','魔法師') and len(Pass_List[i][3]) > 0 \
                and current_date >= datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') \
                and current_date < datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):

                #是否回傳備註
                if len(str(Pass_List[i][5])) >= 0:
                    memostr = str(Pass_List[i][5])
                else:
                    memostr = ''

                if len(Pass_List[i][4]) > 0 and int(Pass_List[i][4]) > 0 and Pass_List[i][1] not in ('魔法師'):
                    passstr = '過[' + Pass_List[i][4] + '] '
                else:
                    passstr = ''

                if len(Pass_List[i][3]) > 0:
                    #Boss_name = '{name:<{len}}\t'.format(name=str(Pass_List[i][1]),len=8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1]).encode('GBK')))
                    Boss_name = str(Pass_List[i][1]).ljust(8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1])))
                    PassStrTemp = PassStrTemp + str(Pass_List[i][3])[11:19] + ' '
                    PassStrTemp = PassStrTemp + Boss_name
                    PassStrTemp = PassStrTemp + passstr
                    PassStrTemp = PassStrTemp + memostr + '\n'
        SplitLine = '{:-^25s}'.format('') + '\n'

        for i in range(0,len(GiantBoss_List)):
            #判斷時間及計算下次重生時間
            if len(GiantBoss_List[i][3]) > 0:
                while current_date > datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=600):
                    GiantBoss_List[i][3] = datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(GiantBoss_List[i][2]))

        #重新存檔
        GiantBoss_List = sorted(GiantBoss_List,key=lambda x:x[3])
        np.save('LineageM/GiantBoss_List', GiantBoss_List)

        if current_date.isoweekday() in (1,2,3,4,5):
            for i in range(0,len(GiantBoss_List)):
                if current_date >= datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=3600) \
                    and current_date < datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):

                    if len(GiantBoss_List[i][3]) > 0 \
                        and (datetime.strptime(GiantBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=60)).isoweekday() in (1,2,3,4,5):
                        #Boss_name = '{name:<{len}}\t'.format(name=str(Pass_List[i][1]),len=8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1]).encode('GBK')))
                        Boss_name = str(GiantBoss_List[i][1]).ljust(8-len(str(GiantBoss_List[i][1]).encode('GBK'))+len(str(GiantBoss_List[i][1])))
                        GiantStrTemp = GiantStrTemp + str(GiantBoss_List[i][3])[11:19] + ' ' #時間
                        GiantStrTemp = GiantStrTemp + Boss_name + '\n'                #王名
        else:
            GiantStrTemp = GiantStrTemp + '本日公休\n'

        for i in range(0,len(StandardBoss_List)):
            #判斷時間及計算下次重生時間
            if len(StandardBoss_List[i][3]) > 0:
                while current_date > datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=600):
                    StandardBoss_List[i][3] = datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(StandardBoss_List[i][2]))

        #重新存檔
        StandardBoss_List = sorted(StandardBoss_List,key=lambda x:x[3])
        np.save('LineageM/StandardBoss_List', StandardBoss_List)

        for i in range(0,len(StandardBoss_List)):
            if current_date >= datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') - dt.timedelta(seconds=3600) \
                and current_date < datetime.strptime(StandardBoss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):

                if len(StandardBoss_List[i][3]) > 0:
                    #Boss_name = '{name:<{len}}\t'.format(name=str(Pass_List[i][1]),len=8-len(str(Pass_List[i][1]).encode('GBK'))+len(str(Pass_List[i][1]).encode('GBK')))
                    Boss_name = str(StandardBoss_List[i][1]).ljust(8-len(str(StandardBoss_List[i][1]).encode('GBK'))+len(str(StandardBoss_List[i][1])))
                    StandardStrTemp = StandardStrTemp + str(StandardBoss_List[i][3])[11:19] + ' ' #時間
                    StandardStrTemp = StandardStrTemp + Boss_name + '\n'                #王名

        setrecord = 0
    #特殊王查詢
    elif askString == '特出':
        sendStringTemp = '特殊王時間表：\n'
        for i in range(0,len(Boss_List)):
            if Boss_List[i][1] in ('海蟲','大腳','螞蟻','巨飛','變怪','卡司特','狼王','不死鳥','古巨','死騎','克特'):

                #判斷時間及計算下次重生時間
                if len(Boss_List[i][3]) > 0:
                    while current_date > datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S'):
                        Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Boss_List[i][2]))
                        Boss_List[i][4] = int(Boss_List[i][4]) + 1

                #重新存檔
                np.save('LineageM/Boss_List_' + checkid, Boss_List)

        Boss_List = sorted(Boss_List,key=lambda x:x[3])

        for i in range(0,len(Boss_List)):
            if Boss_List[i][1] in ('海蟲','大腳','螞蟻','巨飛','變怪','卡司特','狼王','不死鳥','古巨','死騎','克特'):

                if len(Boss_List[i][4]) > 0 and int(Boss_List[i][4]) > 0:
                    passstr = '過[' + Boss_List[i][4] + '] '
                else:
                    passstr = ''

                #是否回傳備註
                if len(str(Boss_List[i][5])) >= 0:
                    memostr = str(Boss_List[i][5])
                else:
                    memostr = ''

                if len(Boss_List[i][3]) > 0:
                    sendStringTemp = sendStringTemp + str(Boss_List[i][3])[11:19] + ' '
                    sendStringTemp = sendStringTemp + str(Boss_List[i][1]) + ' '
                    sendStringTemp = sendStringTemp + passstr
                    sendStringTemp = sendStringTemp + memostr + '\n'

        setrecord = 0
    #前次錯過查詢
    elif askString == '過':
        sendStringTemp = '前次錯過時間表：\n'
        for i in range(0,len(Boss_List)):
            if len(Boss_List[i][4]) > 0 and int(Boss_List[i][4]) > 0:

                #判斷時間及計算下次重生時間
                if len(Boss_List[i][3]) > 0:
                    while current_date > datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S'):
                        Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Boss_List[i][2]))
                        Boss_List[i][4] = int(Boss_List[i][4]) + 1

                #重新存檔
                np.save('LineageM/Boss_List_' + checkid, Boss_List)

        Boss_List = sorted(Boss_List,key=lambda x:x[3])

        for i in range(0,len(Boss_List)):
            if Boss_List[i][1] not in ('浮士德','巴風特','魔法師'):
                if len(Boss_List[i][4]) > 0 and int(Boss_List[i][4]) > 0:
                    passstr = '過[' + Boss_List[i][4] + '] '
                else:
                    passstr = ''

                #是否回傳備註
                if len(str(Boss_List[i][5])) >= 0:
                    memostr = str(Boss_List[i][5])
                else:
                    memostr = ''
                
                if len(Boss_List[i][4]) > 0 and int(Boss_List[i][4]) > 0:
                    if len(Boss_List[i][3]) > 0 and Boss_List[i][1] not in ('魔法師'):
                        sendStringTemp = sendStringTemp + str(Boss_List[i][3])[11:19] + ' '
                        sendStringTemp = sendStringTemp + str(Boss_List[i][1]) + ' '
                        sendStringTemp = sendStringTemp + passstr
                        sendStringTemp = sendStringTemp + memostr + '\n'
        setrecord = 0
    elif askString in '@':
        pass
    #記錄單隻王死亡時間設定
    else:
        #分割字串
        if(askString[0] == '+' and askString[1] != ' '):
            askString = askString.replace('+','+ ')
        LastTimeUpdate = askString.split(" ", 2)
        LastTimeUpdate[0] = LastTimeUpdate[0].replace(':','')
        #查關鍵字用的
        KeyWordString = ''

        if LastTimeUpdate[0].isnumeric() or LastTimeUpdate[0] == '+':
            #時間設定判斷
            if(len(LastTimeUpdate[0]) == 4):
                newtime = LastTimeUpdate[0][0:2] + ':' + LastTimeUpdate[0][2:4] + ':' + '00'
            elif(len(LastTimeUpdate[0]) == 6):
                newtime = LastTimeUpdate[0][0:2] + ':' + LastTimeUpdate[0][2:4] + ':' + LastTimeUpdate[0][4:6]
            elif LastTimeUpdate[0] == '666' or LastTimeUpdate[0] == '+':
                newtime = datetime.now().strftime('%H:%M:%S')
            else:
                setrecord = 0
                pass
            #開機重置
            if len(LastTimeUpdate) > 1:
                if LastTimeUpdate[1].find('開') >= 0 and setrecord == 1:
                    sendStringTemp = '重置出王時間表：\n'
                    for i in range(0,len(Boss_List)):
                        if len(Boss_List[i][3]) == 0 or Boss_List[i][5] == '開':
                            newdatetime = datetime.strptime(datetime.now().strftime('%Y-%m-%d') + ' ' + newtime,'%Y-%m-%d %H:%M:%S')
                            Boss_List[i][3] = newdatetime
                            Boss_List[i][4] = 0
                            Boss_List[i][5] = '開'
                        #判斷時間及計算下次重生時間
                            while current_date > datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S'):
                                Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Boss_List[i][2]))
                                Boss_List[i][4] = int(Boss_List[i][4]) + 1

                        #重新存檔
                        np.save('LineageM/Boss_List_' + checkid, Boss_List)

                    for i in range(0,len(Pass_List)):
                        if len(Pass_List[i][3]) == 0 or Pass_List[i][5] == '開':
                            newdatetime = datetime.strptime(datetime.now().strftime('%Y-%m-%d') + ' ' + newtime,'%Y-%m-%d %H:%M:%S')
                            Pass_List[i][3] = newdatetime
                            Pass_List[i][4] = 0
                            Pass_List[i][5] = '開'
                        #判斷時間及計算下次重生時間
                            while current_date > datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S'):
                                Pass_List[i][3] = datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Pass_List[i][2]))
                                Pass_List[i][4] = int(Pass_List[i][4]) + 1

                        #重新存檔
                        np.save('LineageM/Boss_List_' + checkid, Boss_List)

                    OpenDatetime = datetime.strptime(datetime.now().strftime('%Y-%m-%d') + ' ' + newtime,'%Y-%m-%d %H:%M:%S')
                    np.save('LineageM/WeekOpen_' + checkid, OpenDatetime)
                    
                    Boss_List = sorted(Boss_List,key=lambda x:x[3])

                    for i in range(0,len(Boss_List)):
                        if Boss_List[i][1] not in ('浮士德','巴風特','魔法師'):
                            if int(Boss_List[i][4]) > 0 and Boss_List[i][1] not in ('魔法師'):
                                passstr = '過[' + Boss_List[i][4] + '] '
                            else:
                                passstr = ''
                            
                            #是否回傳備註
                            if len(str(Boss_List[i][5])) >= 0:
                                memostr = str(Boss_List[i][5])
                            else:
                                memostr = ''
                            
                            sendStringTemp = sendStringTemp + (str(Boss_List[i][3])[11:19]) + ' '
                            sendStringTemp = sendStringTemp + str(Boss_List[i][1]) + ' '
                            sendStringTemp = sendStringTemp + passstr + ' '
                            sendStringTemp = sendStringTemp + memostr + '\n'
                    setrecord = 0
                else:
                    pass
                #實際記錄
                if setrecord == 1:
                    newdatetime = datetime.strptime(datetime.now().strftime('%Y-%m-%d') + ' ' + newtime,'%Y-%m-%d %H:%M:%S')

                    #關鍵字有英文的套一下casefold(),然後關鍵字設定為小寫,實際輸入即可不分大小寫判斷
                    #tempIndex拿來存王ID的index,後面會用到
                    #tempPassIndex拿來存王ID的index,後面會用到
                    #RecordIndex拿來存王ID的index,後面會用到
                    #單一BOSS判斷

                    strexists = 0
                    for i in range(0,len(KeyWordList)):
                        KeyWordString = KeyWordList[i][2].split("|")
                        for j in range(0,len(KeyWordString)-1):
                            if LastTimeUpdate[1].casefold() == KeyWordString[j].casefold() or LastTimeUpdate[1].casefold() == KeyWordList[i][1].casefold():
                                strexists = 1
                                tempIndex = np.where(Boss_List == KeyWordList[i][0])[0][0]
                                tempPassIndex = np.where(Pass_List == KeyWordList[i][0])[0][0]
                                RecordIndex = np.where(Record == KeyWordList[i][0])[0][0]
                
                if setrecord == 1:
                    if strexists == 0:
                        sendStringTemp = '清單裡面沒有關於[' + LastTimeUpdate[1] + ']的關鍵字'
                    else:
                        #如果輸入的時間比現在時間大,則減一天
                        if current_date < newdatetime:
                            newdatetime = newdatetime + dt.timedelta(seconds=-86400)
                            nextdatetime = newdatetime + dt.timedelta(seconds=int(Boss_List[tempIndex][2]))
                        else:
                            nextdatetime = newdatetime + dt.timedelta(seconds=int(Boss_List[tempIndex][2]))
                        if Record[RecordIndex][7] != str(newdatetime) + ' ' + userName:
                            for i in range(2,7):
                                Record[RecordIndex][i] = Record[RecordIndex][i + 1]
                            Record[RecordIndex][7] = str(newdatetime) + ' ' + userName
                            np.save('LineageM/RecordList_' + checkid, Record)
                            
                        #把pass改回0
                        Boss_List[tempIndex][4] = 0
                        Pass_List[tempPassIndex][4] = 0
                        
                        while current_date > nextdatetime:
                            nextdatetime = nextdatetime + dt.timedelta(seconds=int(Boss_List[tempIndex][2]))
                            Boss_List[tempIndex][4] = int(Boss_List[tempIndex][4]) + 1
                            Pass_List[tempPassIndex][4] = int(Pass_List[tempPassIndex][4]) + 1

                        if int(Boss_List[tempIndex][4]) > 0:
                            passstr = '過[' + Boss_List[tempIndex][4] + '] '
                        else:
                            passstr = ''

                        sendStringTemp = '已記錄 ' + Boss_List[tempIndex][1] + ' 時間\n'
                        sendStringTemp = sendStringTemp + '死亡時間 ' + str(newdatetime)[5:19] + '\n'
                        sendStringTemp = sendStringTemp + '下次出現 ' + str(nextdatetime)[5:19] + passstr
                        
                        #修改新的時間
                        Boss_List[tempIndex][3] = nextdatetime
                        Pass_List[tempPassIndex][3] = nextdatetime

                        #抓已過還沒打的要先減一輪
                        if newdatetime != nextdatetime - dt.timedelta(seconds=int(Boss_List[tempIndex][2])):
                            Pass_List[tempPassIndex][3] = nextdatetime - dt.timedelta(seconds=int(Boss_List[tempIndex][2]))
                            Pass_List[tempPassIndex][4] = int(Pass_List[tempPassIndex][4]) - 1
                        if len(LastTimeUpdate) >= 3:
                            Boss_List[tempIndex][5] = LastTimeUpdate[2]
                            Pass_List[tempPassIndex][5] = LastTimeUpdate[2]
                        else:
                            Boss_List[tempIndex][5] = ''
                            Pass_List[tempPassIndex][5] = ''
                        
                        for i in range(0,len(Boss_List)):
                            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
                            if Boss_List[i][1] not in ('浮士德','巴風特','魔法師') and len(Boss_List[i][3]) > 0:
                                #是否回傳備註
                                if len(str(Boss_List[i][5])) >= 0:
                                    memostr = str(Boss_List[i][5])
                                else:
                                    memostr = ''

                                #判斷時間及計算下次重生時間
                                while current_date > datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S'):
                                    Boss_List[i][3] = datetime.strptime(Boss_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Boss_List[i][2]))
                                    Boss_List[i][4] = int(Boss_List[i][4]) + 1

                                if int(Boss_List[i][4]) > 0 and Boss_List[i][1] not in ('魔法師'):
                                    passstr = '過[' + Boss_List[i][4] + '] '
                                else:
                                    passstr = ''

                                Boss_List = sorted(Boss_List,key=lambda x:x[3])

                        for i in range(0,len(Pass_List)):
                            #if Boss_List[i][1] not in ('惡魔監視者','浮士德','巴風特') and len(Boss_List[i][3]) > 0:
                            if Pass_List[i][1] not in ('浮士德','巴風特','魔法師') and len(Pass_List[i][3]) > 0:
                                #是否回傳備註
                                if len(str(Pass_List[i][5])) >= 0:
                                    memostr = str(Pass_List[i][5])
                                else:
                                    memostr = ''

                                #判斷時間及計算下次重生時間
                                while current_date > datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=1800):
                                    Pass_List[i][3] = datetime.strptime(Pass_List[i][3],'%Y-%m-%d %H:%M:%S') + dt.timedelta(seconds=int(Pass_List[i][2]))
                                    Pass_List[i][4] = int(Pass_List[i][4]) + 1

                                if int(Pass_List[i][4]) > 0 and Pass_List[i][1] not in ('魔法師'):
                                    passstr = '過[' + Pass_List[i][4] + '] '
                                else:
                                    passstr = ''

                        Pass_List = sorted(Pass_List,key=lambda x:x[3])
                        #重新存檔
                        np.save('LineageM/Boss_List_' + checkid, Boss_List)
                        np.save('LineageM/Pass_List_' + checkid, Pass_List)
                else:
                    pass
            else:
                pass
        elif LastTimeUpdate[0] in ('紀錄','記錄'):
            for i in range(0,len(KeyWordList)):
                KeyWordString = KeyWordList[i][2].split("|")
                for j in range(0,len(KeyWordString)-1):
                    if LastTimeUpdate[1].casefold() == KeyWordString[j].casefold() or LastTimeUpdate[1].casefold() == KeyWordList[i][1].casefold():
                        RecordIndex = np.where(Record == KeyWordList[i][0])[0][0]

            sendStringTemp = Record[RecordIndex][1] + ' 紀錄\n'
            sendStringTemp = sendStringTemp + Record[RecordIndex][7] + '\n'
            sendStringTemp = sendStringTemp + Record[RecordIndex][6] + '\n'
            sendStringTemp = sendStringTemp + Record[RecordIndex][5] + '\n'
            sendStringTemp = sendStringTemp + Record[RecordIndex][4] + '\n'
            sendStringTemp = sendStringTemp + Record[RecordIndex][3] + '\n'
            sendStringTemp = sendStringTemp + Record[RecordIndex][2]
                #keyword
        elif LastTimeUpdate[0].casefold() == 'key':
            keyStr = askString.split(" ")
            sendStringTemp = ('關鍵字清單：\n')
            if askString.casefold() == 'key':
                for i in range(0,len(KeyWordList)):
                    if KeyWordList[i][1] not in ('浮士德','巴風特','魔法師'):
                        Boss_name = str(KeyWordList[i][1]).ljust(8-len(str(KeyWordList[i][1]).encode('GBK'))+len(str(KeyWordList[i][1])))
                        sendStringTemp = sendStringTemp + Boss_name
                        sendStringTemp = sendStringTemp + str(KeyWordList[i][2]) + '\n'
            else:
                for i in range(0,len(KeyWordList)):
                    KeyWordString = KeyWordList[i][2].split("|")
                    for j in range(0,len(KeyWordString)-1):
                        if LastTimeUpdate[1].casefold() == KeyWordString[j].casefold() or LastTimeUpdate[1].casefold() == KeyWordList[i][1].casefold():
                            Boss_name = str(KeyWordList[i][1]).ljust(8-len(str(KeyWordList[i][1]).encode('GBK'))+len(str(KeyWordList[i][1])))
                            sendStringTemp = sendStringTemp + Boss_name
                            sendStringTemp = sendStringTemp + str(KeyWordList[i][2]) + '\n'
            
            setrecord = 0
        elif LastTimeUpdate[0].casefold() == 'add':
            for i in range(0,len(KeyWordList)):
                KeyWordString = KeyWordList[i][2].split("|")
                if LastTimeUpdate[1] == KeyWordList[i][1]:
                    KeyWordList[i][2] = KeyWordList[i][2] + LastTimeUpdate[2] + '|'
                    sendStringTemp = KeyWordList[i][1] + '新增關鍵字：' + LastTimeUpdate[2] + '完成' + '\n'
                    Boss_name = str(KeyWordList[i][1]).ljust(8-len(str(KeyWordList[i][1]).encode('GBK'))+len(str(KeyWordList[i][1])))
                    sendStringTemp = sendStringTemp + Boss_name
                    sendStringTemp = sendStringTemp + str(KeyWordList[i][2]) + '\n'

            np.save('LineageM/KeywordList_' + checkid, KeyWordList)        

            setrecord = 0
        elif LastTimeUpdate[0].casefold() == 'del':
            for i in range(0,len(KeyWordList)):
                KeyWordString = KeyWordList[i][2].split("|")
                if LastTimeUpdate[1] == KeyWordList[i][1]:
                    KeyWordList[i][2] = KeyWordList[i][2].replace(LastTimeUpdate[2] + '|','')
                    sendStringTemp = KeyWordList[i][1] + '　刪除關鍵字：' + LastTimeUpdate[2] + '完成' + '\n'
                    Boss_name = str(KeyWordList[i][1]).ljust(8-len(str(KeyWordList[i][1]).encode('GBK'))+len(str(KeyWordList[i][1])))
                    sendStringTemp = sendStringTemp + Boss_name
                    sendStringTemp = sendStringTemp + str(KeyWordList[i][2]) + '\n'
            
            np.save('LineageM/KeywordList_' + checkid, KeyWordList)        

            setrecord = 0
        else:
            pass

    #if len(PassStrTemp) > 0:
    #    PassStrTemp = PassStrTemp + '\n'
    #else:
    #    PassStrTemp = ''
    return PassStrTemp + SplitLine + GiantStrTemp + SplitLine + StandardStrTemp + SplitLine + sendStringTemp