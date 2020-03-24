# -*- coding: utf-8 -*-

import time
import json

def saveToFile(content):
    f = open("./goods.txt", "a")
    f.write('\n')
    f.write(content)
    f.close()

if __name__ == '__main__':
    timeMilli = '1584887769284'
    title = '天猫 李子柒杏鲍菇牛肉酱香辣拌饭拌面酱下饭杂酱面辣椒酱220g*2'
    title_span = '天猫'
    new_price = '￥67.7'
    old_price = '￥67.7'
    saller = '销量33522'
    money = ''
    content = '复制此条信息，(95y617xVUXj),打开【手机淘宝即可查看】'


    goodDict = {}
    goodDict['creatTime'] = timeMilli
    goodDict['title'] = title
    goodDict['title_span'] = title_span
    goodDict['new_price'] = new_price
    goodDict['old_price'] = old_price
    goodDict['saller'] = saller
    goodDict['money'] = money
    goodDict['content'] = content

    goodStr = json.JSONEncoder().encode(goodDict)

    print(goodStr)

    saveToFile(goodStr)