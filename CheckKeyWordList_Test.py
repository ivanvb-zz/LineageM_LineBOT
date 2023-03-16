###王表關鍵字設定###

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

filepath = "LineageM/KeywordList.npy"

sendStringTemp = ''

if os.path.isfile(filepath):                #檔案在就讀取
    KeyWordList = np.load('LineageM/KeywordList.npy')
    askString = 'del 變怪 變'
    KeyWordString = ''
    LastTimeUpdate = askString.split(" ",2)
    keyStr = askString.split(" ")
    sendStringTemp = ('關鍵字清單：\n')
    if LastTimeUpdate[0] == 'del':
        for i in range(0,len(KeyWordList)):
            KeyWordString = KeyWordList[i][2].split("|")
            if LastTimeUpdate[1] == KeyWordList[i][1]:
                KeyWordList[i][2] = KeyWordList[i][2].replace(LastTimeUpdate[2] + '|','')
                print(KeyWordList[i])
                
else:                                       #第一次執行要建出王清單檔案
    KeyWordList = np.array([
        ['Boss_04','死騎','04|死亡騎士|死騎|'],
        ['Boss_05','海蟲','5|05|蟲|蜈蚣|'],
        ['Boss_26','螞蟻','26|螞蟻|'],
        ['Boss_28','強盜','28|強盜|'],
        ['Boss_35','蜘蛛','35|蜘蛛|'],
        ['Boss_44','鱷魚','44|鱷魚|'],
        ['Boss_62','大腳','62|腳|'],
        ['Boss_70','古巨','70|巨人|古巨|'],
        ['Boss_73','巨飛','73|巨飛|'],
        ['Boss_74','74','74|'],
        ['Boss_76','76','76|'],
        ['Boss_771','77下','771|77左|77下|下|'],
        ['Boss_772','77上','772|77右|77上|上|'],
        ['Boss_773','大黑','773|大黑|黑老|'],
        ['Boss_Bird','鳥','鳥|'],
        ['Boss_EF','EF','39|EF|伊弗|一佛|'],
        ['Boss_G','小綠','47|G|綠|'],
        ['Boss_R','小紅','48|472|R|紅|'],
        ['Boss_Orcus','烏勒','烏勒|'],
        ['Boss_Tree','樹精','20|21|50|樹|'],
        ['Boss_Doppelganger','變怪','61|變|'],
        ['Boss_Four','四色','4|68|四色|'],
        ['Boss_304','304','304|'],
        ['Boss_General','將軍','72|將軍|港口|貝|'],
        ['Boss_Wolf','力卡溫','19|狼|力卡溫|'],
        ['Boss_Kete','克特','12|克特|'],
        ['Boss_Caster','卡王','22|卡|'],
        ['Boss_Devil','監視者','7|監視者|'],
        ['Boss_Rabbit','兔','兔|'],
        ['Boss_Necuros','奈克','奈克']
        ])
    np.save('LineageM/KeywordList', KeyWordList)