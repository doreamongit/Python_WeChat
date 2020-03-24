# -*- coding: utf-8 -*-

from selenium import webdriver
# 用于设置等待时间
from selenium.webdriver.support.wait import WebDriverWait
# 用于匹配节点
from selenium.webdriver.common.by import By
# 用于等待时判断节点是否加载，如果没有，继续在规定的时间加载
from selenium.webdriver.support import expected_conditions as EC

import time
import json

browser = webdriver.Chrome()

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

        print(title)
        print(title_span)
        print(new_price)
        print(old_price)
        print(saller)
        print(money)
        print(content)
        print(timeMilli)
        print(imageURLs)

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

        # goodStr=json.JSONEncoder().encode(goodDict).decode('utf-8')
        goodStr = json.dumps(goodDict,ensure_ascii=False)

        print(goodStr)

        saveToFile(goodStr)

    finally:
        # 关闭浏览器
        # browser.close()
        pass

def saveToFile(content):
    f = open("./goods.json", "a")
    f.write('\n')
    f.write(content)
    f.close()


if __name__ == '__main__':
    # getHttpWithSelenium(
    #     u'https://share-miyuan-1194.kuaizhan.com/#/goodDetail?tkl=(Q46Y17b15N1)&itemSource=1&invite_code=MGIDFQ&id=577460300572&token=kzsjwybs')
    # getHttpWithSelenium(
    #     u'https://share-miyuan-1194.kuaizhan.com/#/goodDetail?tkl=(Q46Y17b15N1)&itemSource=1&invite_code=MGIDFQ&id=577460300572&token=kzsjwybs')
    getHttpWithSelenium(
        u'https://share-miyuan-1194.kuaizhan.com/#/goodDetail?tkl=%28o8LP17CNuq7%29&itemSource=1&invite_code=MGIDFQ&id=608189785003&token=kzsjwybs')
