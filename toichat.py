#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# Author: chenshy
# @Time    : 2018/3/9 15:59


import itchat, time
import requests
from jieping import capture
import datetime
import sched

itchat.auto_login(hotReload=True)

# 发送给公众号 success

# user = itchat.search_friends(name=u'LittleCoder机器人')[0]
# print user
# user.send('greeting, littlecoder!')


# 发送给群聊 succes

# mpsList=itchat.get_chatrooms(update=True)[1:]
# print mpsList
# # itchat.run()
# total=0
# for it in mpsList:
#     print(it['NickName'])
#     total=total+1
#
# 群聊只会显示最近活跃的项
# room = itchat.search_chatrooms(name=u'19号楼1603')[0]
# print room
# room.send(u'greeting, 明!')
# itchat.dump_login_status()

# 发送给自己 success
# print itchat.search_friends()
# itchat.send('Hello2!')



# 文件传输助手   success
# itchat.send('Hello3!', toUserName='filehelper')

url = 'http:/xxxxx'
a = requests.get(url)
capture(url, save_fn='test1.png')


def sendIcart():
    if a.status_code == 200:
        mpsList = itchat.get_chatrooms(update=True)[1:]
        room = itchat.search_chatrooms(name=u'楼603')[0]
        # room = itchat.search_friends()
        print room
        room.send("@img@%s" % 'test1.png')
        utext = unicode("%s月%s日%s点%s分%s秒" % (
            datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().hour,
            datetime.datetime.now().minute, datetime.datetime.now().second) + '网站无异常', "utf8")
        room.send(utext)

schedule = sched.scheduler(time.time, time.sleep)
for i in range(13):
    schedule.enter(900 * i, 0, sendIcart, ())

schedule.run()
