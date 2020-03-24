# -*- coding: utf-8 -*-
from wxpy import *
import json
import urllib.request
import random
import string

# 初始化机器人
bot = Bot(console_qr=False, cache_path=True)

tuling='dbfd66e5cd314db091d2befcb7c5dd67'
api_url = "http://openapi.tuling123.com/openapi/api/v2"

def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return salt

userid = ranstr(32)

def initRob():
    bot = Bot(console_qr=False, cache_path=True)


# company_group = bot.groups().search(u'celery2011,雨,简单,珍')[0]
company_group = bot.groups().search(u'👸家用品淘宝撸单')[0]

# 注册机器人监听文件助手
@bot.register(bot.file_helper, except_self=False)
def reply_file_helper(msg):
    print(msg.sender)
    print('收到[{}]消息: {} ({})'.format(msg.sender, msg.text, msg.type))
    if msg.type == 'Text' :
        msg.forward(company_group, prefix='')
        # tulingRes = get_message(msg.text,userid)
        # print('图灵回复:'+tulingRes)


def get_message(message,userid):
    req = {
    "perception":
        {
            "inputText":
            {
                "text": message
            },

            "selfInfo":
            {
                "location":
                {
                    "city": "深圳",
                    "province": "广州",
                    "street": "XXX"
                }
            }
        },
        "userInfo": 
        {
            "apiKey": tuling,
            "userId": userid
        }
    }
    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)
    results_text = response_dic['results'][0]['values']['text']
    return results_text

if __name__ == '__main__':
    # initRob()

    embed()