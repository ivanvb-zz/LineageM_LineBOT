from numpy import *
import numpy as np
import os

filepath = "LineageM/PartyList.npy"

if os.path.isfile(filepath):                #檔案在就讀取
    Boss_List = np.load('LineageM/PartyList.npy',allow_pickle=True)
else:                                       #第一次執行要建出王清單檔案
    Boss_List = np.array([], dtype=object)
    np.save('LineageM/PartyList', Boss_List)