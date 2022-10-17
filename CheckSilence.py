###王表回應初始化設定###
from numpy import *
import numpy as np
import os

def SilenceListCheck(GroupID):
# 要檢查的檔案路徑
    filepath = "LineageM/Silence_" + GroupID + ".npy"

    if os.path.isfile(filepath):                #檔案在就讀取
        silence_tag = np.load('LineageM/Silence_' + GroupID + '.npy')
    else:                                       #第一次執行要建出王清單檔案
        silence_tag = 1
        np.save('LineageM/Silence_' + GroupID, silence_tag)