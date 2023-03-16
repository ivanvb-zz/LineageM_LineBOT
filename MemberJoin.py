###成員名單設定###

#字串處理
import configparser

#陣列
import collections
from tkinter.simpledialog import askstring
from numpy import *
import numpy as np
from numpy.core.defchararray import isdigit 

#本機資源
import os
#import PartyList
import MemberList

#Party_List = np.load('LineageM/PartyList.npy',allow_pickle=True)
#Member_List = np.load('LineageM/MemberList.npy',allow_pickle=True)

def MemberSet(askString,userName):
    Member_List = np.load('LineageM/MemberList.npy',allow_pickle=True)
    #askString = input()
    askstr = askString.split(" ", 2)
    if len(askstr) > 1:
        MemberName = askstr[1]
    returnStr = ''
    if askstr[0] == '血盟指令':
        returnStr = ('血盟指令說明(@表示空格)：\n')
        returnStr = returnStr + '新增成員：新增成員@角色名稱\n'
        returnStr = returnStr + '修改成員：修改成員@舊角色名稱@新角色名稱\n'
        returnStr = returnStr + '刪除成員：刪除成員@角色名稱\n'
        returnStr = returnStr + '修改職業：成員職業@角色名稱@角色職業\n'
        returnStr = returnStr + '修改血盟：成員血盟@角色名稱@血盟名稱\n'
        returnStr = returnStr + 'Line對應：成員賴@角色名稱@Line名稱\n'
        returnStr = returnStr + '成員查詢：成員\n'
        returnStr = returnStr + '血盟查詢：血盟@血盟名稱\n'
        returnStr = returnStr + '職業查詢：職業@職業名稱(待開發)\n'
        returnStr = returnStr + '職業對照：供設定成員職業使用'
    elif askstr[0] == '職業對照':
        returnStr = ('職業對照(需設定正確職業才可使用職業查詢功能)：\n')
        returnStr = returnStr + '王族　　：王\n'
        returnStr = returnStr + '騎士　　：騎\n'
        returnStr = returnStr + '法師　　：法\n'
        returnStr = returnStr + '妖精　　：妖\n'
        returnStr = returnStr + '神聖劍士：聖劍\n'
        returnStr = returnStr + '狂戰士　：狂戰\n'
        returnStr = returnStr + '死神　　：死神\n'
        returnStr = returnStr + '黑暗妖精：黑妖\n'
        returnStr = returnStr + '龍鬥士　：龍鬥\n'
        returnStr = returnStr + '槍手　　：槍手\n'
        returnStr = returnStr + '暗黑騎士：暗騎\n'
    elif askstr[0] == '新增成員':
        if len(np.where(Member_List == MemberName)[0]) == 0:
            if str(MemberName)[0:1] == '@':
                returnStr = '請輸入正確角色名稱'
            else:
                if len(Member_List) == 0:
                    Member_List = np.vstack(Member_List,[MemberName,'','',userName])
                else:
                    Member_List = np.vstack([Member_List,[MemberName,'','',userName]])
                returnStr = '已新增成員，其遊戲內名稱為：' + MemberName
        else:
            returnStr = '該成員已存在'
    elif askstr[0] == '修改成員':
        MemberNewName = askstr[2]
        if len(np.where(Member_List == MemberName)[0]) == 0:
            returnStr = '該成員不存在,請先設定成員'
        else:
            Member_List[np.where(Member_List == MemberName)[0][0]][0] = MemberNewName
            returnStr = '成員 ' + MemberName + ' 已修改為：' + MemberNewName
    elif askstr[0] == '刪除成員':
        if len(np.where(Member_List == MemberName)[0]) == 0:
            returnStr = '該成員不存在'
        else:
            for i in range(0,3):
                Member_List[np.where(Member_List == MemberName)[0][0]][i] = ''
            returnStr = '成員 ' + MemberName + ' 已刪除'
    elif askstr[0] == '成員職業':
        RoleName = askstr[2]
        if len(np.where(Member_List == MemberName)[0]) == 0:
            returnStr = '該成員不存在,請先設定成員'
        else:
            Member_List[np.where(Member_List == MemberName)[0][0]][1] = RoleName
            returnStr = '變更成員 ' + MemberName + ' 職業為：' + RoleName
    elif askstr[0] == '成員血盟':
        PartyName = askstr[2]
        if len(np.where(Member_List == MemberName)[0]) == 0:
            returnStr = '該成員不存在,請先設定成員'
        else:
            Member_List[np.where(Member_List == MemberName)[0][0]][2] = PartyName
            returnStr = '變更成員 ' + MemberName + ' 血盟為：' + PartyName
    elif askstr[0] == '成員Line' or askstr[0] == '成員賴':
        LineName = askstr[2]
        if len(np.where(Member_List == MemberName)[0]) == 0:
            returnStr = '該成員不存在,請先設定成員'
        else:
            Member_List[np.where(Member_List == MemberName)[0][0]][3] = LineName
            returnStr = '變更成員 ' + MemberName + ' Line對應為：' + LineName
    elif askstr[0] == '血盟':
        PartyName = askstr[1]
        for i in range(0,len(Member_List)):
            if Member_List[i][2].find(PartyName) >= 0:
                returnParty = '[' + Member_List[i][2] + ']'
                rerutnRole = '(' + Member_List[i][1] + ')'
                rerutnMemberName = Member_List[i][0]
                rerutnLineName = Member_List[i][3]
                returnStr = returnStr + returnParty + rerutnRole + rerutnMemberName + '：' + rerutnLineName + '\n'
    elif askstr[0] == '職業':
        RoleName = askstr[1]
        for i in range(0,len(Member_List)):
            if Member_List[i][1].find(RoleName) >= 0:
                returnParty = '[' + Member_List[i][2] + ']'
                rerutnRole = '(' + Member_List[i][1] + ')'
                rerutnMemberName = Member_List[i][0]
                rerutnLineName = Member_List[i][3]
                returnStr = returnStr + returnParty + rerutnRole + rerutnMemberName + '：' + rerutnLineName + '\n'
    elif askstr[0] == '成員':
        for i in range(1,len(Member_List)):
            if len(Member_List[i][0]) > 0:
                returnParty = '[' + Member_List[i][2] + ']'
                rerutnRole = '(' + Member_List[i][1] + ')'
                rerutnMemberName = Member_List[i][0]
                rerutnLineName = Member_List[i][3]
                returnStr = returnStr + returnParty + rerutnRole + rerutnMemberName + '：' + rerutnLineName + '\n'

    np.save('LineageM/MemberList', Member_List)
    return returnStr