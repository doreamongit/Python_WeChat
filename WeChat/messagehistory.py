# -*- coding: utf-8 -*-
from wxpy import *

# 初始化机器人
bot = Bot(console_qr=False, cache_path=True)

def get_history_message():
    sent_msgs = bot.messages.search(sender=bot.self)
    print(sent_msgs)
    


if __name__ == '__main__':
    get_history_message()

    embed()