###奇岩地監王初始化設定###
from numpy import *
import numpy as np
import os

#產生王表

#[0]:代碼
#[1]:名稱
#[2]:重生時間(分)
#[3]:最近一次回報
#[4]:錯過次數
#[5]:備註

# 要檢查的檔案路徑
filepath = "D:/LineageM/StandardBoss_List.npy"

if os.path.isfile(filepath):                #檔案在就讀取
    Boss_List = np.load('D:/LineageM/StandardBoss_List.npy')
else:                                       #第一次執行要建出王清單檔案
    Boss_List = np.array([
        ['Standard_01','魔法師',7200,'2021-11-30 05:00:00',0,''],
        ['Standard_02_14','巴風特(30分)',86400,'2021-11-30 14:00:00',0,''],
        ['Standard_02_20','巴風特(30分)',86400,'2021-11-30 20:00:00',0,''],
        ['Standard_03','三王(9-24-15)',86400,'2021-11-30 19:15:00',0,''],
        ['Standard_04','EJ',86400,'2021-11-30 23:00:00',0,''],
        ['Standard_05','大死騎',86400,'2021-11-30 23:30:00',0,''],
        ['Standard_06','軍團長(修練4)',86400,'2021-11-30 18:00:00',0,''],
        ['Standard_07','德拉卡利斯(修練4)',86400,'2021-11-30 00:00:00',0,''],
        ['Standard_08','惡魔',86400,'2021-11-30 22:00:00',0,'']
        ])
    np.save('D:/LineageM/StandardBoss_List', Boss_List)