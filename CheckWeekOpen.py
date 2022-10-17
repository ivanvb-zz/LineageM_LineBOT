###開機時間初始化設定###
from numpy import *
import numpy as np
import os

from datetime import datetime
import datetime as dt

# 要檢查的檔案路徑
def WeekOpenCheck(GroupID):
    filepath = "LineageM/WeekOpen_" + GroupID + ".npy"

    if os.path.isfile(filepath):                #檔案在就讀取
        OpenDatetime = np.load('LineageM/WeekOpen_' + GroupID + '.npy',allow_pickle=True)
    else:                                       #第一次執行要建出王清單檔案
        OpenDatetime = ''
        np.save('LineageM/WeekOpen_' + GroupID, OpenDatetime)