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
filepath = "D:/LineageM/GiantBoss_List.npy"

if os.path.isfile(filepath):                #檔案在就讀取
    Boss_List = np.load('D:/LineageM/GiantBoss_List.npy')
else:                                       #第一次執行要建出王清單檔案
    Boss_List = np.array([
        ['Giant_01_06','奇一',86400,'2021-11-30 06:00:00',0,''],
        ['Giant_01_12','奇一',86400,'2021-11-30 12:00:00',0,''],
        ['Giant_01_18','奇一',86400,'2021-11-30 18:00:00',0,''],
        ['Giant_01_00','奇一',86400,'2021-11-30 00:00:00',0,''],
        ['Giant_02_07','奇二',86400,'2021-11-30 07:00:00',0,''],
        ['Giant_02_14','奇二',86400,'2021-11-30 14:00:00',0,''],
        ['Giant_02_21','奇二',86400,'2021-11-30 21:00:00',0,''],
        ['Giant_03','奇三',86400,'2021-11-30 20:15:00',0,''],
        ['Giant_04','奇四',86400,'2021-11-30 21:15:00',0,'']
        ])
    np.save('D:/LineageM/GiantBoss_List', Boss_List)