#字串處理
import configparser

#時間
from datetime import datetime
import datetime as dt

#陣列
import collections
from tkinter.simpledialog import askstring
from numpy import *
import numpy as np
from numpy.core.defchararray import isdigit 

#本機資源
import os
import PartyList
import MemberList

#Party_List = np.load('LineageM/PartyList.npy',allow_pickle=True)
#Member_List = np.load('LineageM/MemberList.npy',allow_pickle=True)

Member_List = np.load('LineageM/Silence.npy',allow_pickle=True)

print(Member_List)