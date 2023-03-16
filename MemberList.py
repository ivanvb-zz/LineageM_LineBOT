###成員名單初始化設定###

from numpy import *
import numpy as np
import os

filepath = "LineageM/MemberList.npy"

if os.path.isfile(filepath):                #檔案在就讀取
    Boss_List = np.load('LineageM/MemberList.npy',allow_pickle=True)
else:                                       #第一次執行要建出王清單檔案
    Boss_List = np.array([['川寶寶','','','Derrick Shih'],
 ['牛奶乄嘎嘣脆','死神','',''],
 ['牛奶乄冰刺','','',''],
 ['牛奶乄朱紗丸','','',''],
 ['牛奶乄吃蘋果','妖精','','雨'],
 ['牛奶乄金蘋果','法師','','大軒'],
 ['牛奶乄蛤啥洨','','',''],
 ['牛奶乄松果','','',''],
 ['牛奶乄水雲朵','死神','',''],
 ['牛奶乄啃蘋果','','',''],
 ['打雜劉小翔','法','花閣','打雜小弟劉小翔'],
 ['酶','妖','花閣','幾米'],
 ['回憶裡待續','聖劍','花閣','良河'],
 ['古玄怒雲極','妖','花閣','宏'],
 ['嗜血刀','聖劍','花閣','丁永倫'],
 ['紙糊','法','花閣','紙糊'],
 ['乄頑皮豹乄','聖劍','花閣',''],
 ['五告散','死神','花閣','小竹'],
 ['乄尼莫乄','法','花閣','Elsa薰'],
 ['甜芯','王','花閣',''],
 ['乄倫弟乄','法','花閣','辰辰'],
 ['金大遠','妖','花閣','遠'],
 ['牛奶乄跑轟','聖劍','蔓越梅','阿信'],
 ['牛奶乄歸剛欸','妖','蔓越梅',''],
 ['牛奶乄橙果','妖','蔓越梅','邱鈵元'],
 ['牛奶乄咬蘋果','死神','蔓越梅','Di'],
 ['牛奶乄錆兔','死神','蔓越梅',''],
 ['北港6尺4','','蔓越梅','宏'],
 ['牛奶乄小波妞','','蔓越梅',''],
 ['牛奶乄默默','槍','蔓越梅','義'],
 ['牛奶乄雷丸子',' 法師','蔓越梅',''],
 ['牛奶乄青蘋果','死神','蔓越梅','懋'],
 ['牛奶乄嗒咩良','死神','蔓越梅','政憲'],
 ['牛奶乄雷飄飄','妖精','蔓越梅','君君Sandy Huang-地表最強�💕'],
 ['牛奶乄雷果','法師','蔓越莓','阿啾'],
 ['牛奶乄公牛鯊','法師','蔓越莓','Portgas D Gao'],
 ['牛奶乄金無聊','死神','蔓越莓',''],
 ['牛奶乄爆米花','','蔓越梅',''],
 ['牛奶〥小綿羊','','','']], dtype=object)
    np.save('LineageM/MemberList', Boss_List)