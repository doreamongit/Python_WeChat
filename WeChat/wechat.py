# -*- coding: utf-8 -*-

import json
import requests
from wxpy import *
import pyzbar.pyzbar as pyzbar
import io
from PIL import Image,ImageEnhance

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 用于设置等待时间
from selenium.webdriver.common.by import By  # 用于匹配节点
from selenium.webdriver.support import expected_conditions as EC  # 用于等待时判断节点是否加载，如果没有，继续在规定的时间加载
import time

browser = webdriver.Chrome()
# 初始化机器人
bot = Bot(console_qr=False, cache_path=True)

def getHttpWithSelenium(urlPram):
    try:
        browser.get(urlPram)
        wait = WebDriverWait(browser, 10)  # 等待页面加载
        # 判断页面是否响应到id属性为content_left的内容
        # 写的时候是以元组形式 注意括号的个数
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div')))

        title = browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[3]/div').text

        title_span = ''
        try:
            title_span = browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[3]/div/span').text
        except:
            pass

        # 获取商品图片
        imageURLs = []
        try:
            imagesParent = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div')
            images = imagesParent.find_elements_by_tag_name('img')
            for image in images:
                imageURL = image.get_attribute('src')
                if imageURL not in imageURLs:
                    imageURLs.append(imageURL)
        except:
            pass

        old_price = ''
        try:
            old_price = browser.find_element_by_class_name('old-price').text
        except:
            pass

        new_price = ''
        try:
            new_price = browser.find_element_by_class_name('new-price').text
        except:
            pass

        saller = ''
        try:
            saller = browser.find_element_by_class_name('saller').text
        except:
            pass

        money = ''
        try:
            money = browser.find_element_by_class_name('money').text
        except:
            pass

        content = ''
        try:
            content = browser.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[4]/div/div[2]/div[2]').text
        except:
            pass

        timeMilli = str(int(round(time.time() * 1000)))

        # print(title)
        # print(title_span)
        # print(new_price)
        # print(old_price)
        # print(saller)
        # print(money)
        # print(content)
        # print(timeMilli)
        # print(imageURLs)

        goodDict = {}
        goodDict['creatTime'] = timeMilli
        goodDict['title'] = title
        goodDict['title_span'] = title_span
        goodDict['new_price'] = new_price
        goodDict['old_price'] = old_price
        goodDict['saller'] = saller
        goodDict['money'] = money
        goodDict['content'] = content
        goodDict['images'] = imageURLs

        goodStr = json.JSONEncoder().encode(goodDict)
        # print(goodStr)
        saveToFile(goodStr)


    finally:
        # 关闭浏览器
        # browser.close()
        pass

def initRob():
    bot = Bot(console_qr=False, cache_path=True)
    # 定位公司群
    company_group = bot.groups().search(u' 🥚🥚蜜源🐝新人0⃣元购')[0]

    # # 定位老板
    bossBot = company_group.search(u'复制标题')[0]
    bossAssit = company_group.search(u'蛋总小助理-小郑')[0]
    relayBot = company_group.search(u'转播号')[0]
    boss = company_group.search(u'想挣钱找我来培训群')[0]

    # # 将老板的消息转发到文件传输助手
    @bot.register(company_group)
    def forward_boss_message(msg):
        print('收到[{}]消息: {} ({})'.format(msg.sender, msg.text, msg.type))
        if msg.member == boss:
            msg.forward(bot.file_helper, prefix='老板发言')
        if msg.member == bossBot:
            msg.forward(bot.file_helper, prefix='机器人')
        if msg.member == bossAssit:
            msg.forward(bot.file_helper, prefix='助理')
        if msg.member == relayBot:
            msg.forward(bot.file_helper, prefix='转播号')

# 初始化机器人
# def initFileHelpBot():
#     bot = Bot(console_qr=False, cache_path=True)

# 注册机器人监听文件助手
@bot.register(bot.file_helper,except_self=False)
def reply_file_helper(msg):
    print(msg.sender)
    print('收到消息: {} ({})'.format(msg.text, msg.type))

    if msg.type == 'Picture' :
        filedata = msg.get_file()

        encoded_jpg_io = io.BytesIO(filedata)
        image = Image.open(encoded_jpg_io)
        # image.show()

        barcodes = pyzbar.decode(image)
        # print(barcodes)
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            # print(barcodeData)
            getHttpWithSelenium(barcodeData)

def saveToFile(content):
    f = open("./goods.json", "a")
    f.write('\n')
    f.write(content)
    f.close()


if __name__ == '__main__':
    # initFileelpBot()
    initRob()
    embed()
