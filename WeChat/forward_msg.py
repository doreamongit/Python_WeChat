from wxpy import *
# 初始化机器人
bot = Bot(console_qr=False, cache_path=True)

home_shop = bot.groups().search(u'👸家用品淘宝撸单')[0]

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
        if msg.member == boss or msg.member == bossBot or msg.member == bossAssit or msg.member == relayBot:
            msg.forward(home_shop, prefix='')
