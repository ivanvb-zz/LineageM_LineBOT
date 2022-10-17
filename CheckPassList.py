###30分鐘內未打王表初始化設定###

from numpy import *
import numpy as np
import os

from datetime import datetime
#產生王表

#[0]:代碼
#[1]:名稱
#[2]:重生時間(分)
#[3]:最近一次回報
#[4]:錯過次數
#[5]:備註

# 要檢查的檔案路徑

def PassListCheck(GroupID):
    current_date = str(datetime.now())[0:19]
    filepath = "LineageM/Pass_List_" + GroupID + ".npy"

    if os.path.isfile(filepath):                #檔案在就讀取
        Pass_List = np.load('LineageM/Pass_List_' + GroupID + '.npy')
    else:                                       #第一次執行要建出王清單檔案
        Pass_List = np.array([
            ['Boss_04','死騎',32400,current_date,0,''],
            ['Boss_05','海蟲',7200,current_date,0,''],
            ['Boss_26','螞蟻',12600,current_date,0,''],
            ['Boss_28','強盜',10800,current_date,0,''],
            ['Boss_35','蜘蛛',14400,current_date,0,''],
            ['Boss_44','鱷魚',10800,current_date,0,''],
            ['Boss_62','大腳',10800,current_date,0,''],
            ['Boss_70','古巨',30600,current_date,0,''],
            ['Boss_73','巨飛',21600,current_date,0,''],
            ['Boss_74','74',10800,current_date,0,''],
            ['Boss_76','76',10800,current_date,0,''],
            ['Boss_771','77下',7200,current_date,0,''],
            ['Boss_772','77上',7200,current_date,0,''],
            ['Boss_773','大黑',10800,current_date,0,''],
            ['Boss_Bird','不死鳥',28800,current_date,0,''],
            ['Boss_EF','伊弗',7200,current_date,0,''],
            ['Boss_G','小綠',7200,current_date,0,''],
            ['Boss_R','小紅',7200,current_date,0,''],
            ['Boss_Orcus','烏勒(19)',21600,current_date,0,''],
            ['Boss_Tree','樹精',10800,current_date,0,''],
            ['Boss_Doppelganger','變怪',25200,current_date,0,''],
            ['Boss_Four','四色',7200,current_date,0,''],
            ['Boss_304','賽尼斯',10800,current_date,0,''],
            ['Boss_General','將軍',21600,current_date,0,''],
            ['Boss_Wolf','狼王',28800,current_date,0,''],
            ['Boss_Kete','克特',36000,current_date,0,''],
            ['Boss_Caster','卡司特',27000,current_date,0,''],
            ['Boss_Devil','監視者',21600,current_date,0,''],
            ['Boss_Rabbit','兔王',10800,current_date,0,''],
            ['Boss_Necuros','奈克(49)',14400,current_date,0,''],
            ['Boss_Baphomet','巴風特',21600,current_date,0,'']
            ])
        np.save('LineageM/Pass_List_' + GroupID, Pass_List)