# /usr/bin/python
# -*- coding:UTF-8 -*-

import random


# 生成员工列表
def generatelist(num):
    persons = []
    for i in range(1, num + 1):
        persons.append(i)
    return persons


# 抽奖方法 中奖人数，抽奖列表
def getaward(num):
    awardlist = []
    for i in range(1, num + 1):
        rand = random.randint(0, len(employeelist)-1)
        awardlist.insert(i, employeelist[rand])
        del employeelist[rand]
    return awardlist

employeelist = generatelist(200)
print("中一等奖的人有:"+str(getaward(3)))
print("中二等奖的人有:"+str(getaward(10)))
print("中参与奖的人有:"+str(getaward(20)))
