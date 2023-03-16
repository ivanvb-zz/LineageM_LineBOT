
#字串處理
import configparser

#時間
from datetime import datetime
import datetime as dt

#陣列
import collections
from turtle import left
from numpy import *
import numpy as np
from numpy.core.defchararray import isdigit 

#本機資源
import os

###主程式###



import requests
#是否暫停回應
#Member_List = np.load('LineageM/GiantBoss_List.npy',allow_pickle=True)
#print(Member_List)

Boss_List = np.load('LineageM/Boss_List_C9b459635d139461ecbce3a368ac21542.npy')


#Boss_List[4][1] = '77上(772)'
#Boss_List[4][2] = 7200
#Boss_List[5][1] = '77下(771)'
#Boss_List[5][2] = 7200

#current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#print(current_date)

'''
Cffb6b6d9803657ef096cdbb3286e148d:打爆
Ubd9ed8a37a5a51fe3da408c9359883a9:波多野小教室
C170c945b6592d42bb53aac14747edf12:水蛇王表
Cbd816f538c007ac5fed24fada5eb1d4b:水蛇小王表
C9b459635d139461ecbce3a368ac21542:布魯迪卡小王表
C036ed4d1b17ac0df40fe42e776a4f479:半人馬小王表
C6a2a470757e902298da9e4d03eeadca7:布魯迪卡小王表对照表
Cd4de4138f400161d73d3615d9b7b76a3:海胆
'''

checkid = 'Cd4de4138f400161d73d3615d9b7b76a3'
#
Boss_List = np.load('LineageM/Pass_List_' + checkid + '.npy',allow_pickle=True)

'''
for i in range(0,len(Boss_List)):
    if Boss_List[i][0] == 'Boss_Wolf':
        Boss_List[i][2] = 14400
np.save('LineageM/Pass_List_' + checkid, Boss_List)
'''
print(Boss_List)

'''
channel_access_token = 'IuZDQ7Afa71I4p3SIpKaQB/rgompmOTciSqBYAIRHURxkZJ5jNzJ3rnpM23goDCS0LHYrZL9mxob5sqKiJrg9dDzejUyVdZYKojwnUhnwWEm3yTWzmpoNyDOy1X8YQmqYrJibqlMYMFKnYYTAiVDTQdB04t89/1O/w1cDnyilFU='

headers = {"content-type": "application/json; charset=UTF-8",'Authorization':'Bearer {}'.format(channel_access_token)}
url = 'https://api.line.me/v2/bot/group/Cba168781c5fcb16260e7f33c2eafb418/member/U21da7f5adebe99a7c981d0b193c8b6f2'
response = requests.get(url, headers=headers)
response = response.json()
userName = response['displayName']
print(userName)
'''
#np.save('LineageM/Boss_List.npy', Boss_List)


#for i in range(1,len(Member_List)):
    #if len(Member_List[i][0]) == 0:
        #print(Member_List[i])
#Member_List = np.delete(Member_List,predeleteindex) 
#print(Member_List)
#Record = sorted(Record,key=lambda x:x[2])
#np.save('LineageM/MemberList', Record)