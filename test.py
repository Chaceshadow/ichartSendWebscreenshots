#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import itchat
import datetime
import time
from time import sleep
import sched

# itchat.auto_login()
#
# itchat.send('Hello, filehelper', toUserName='filehelper')



# print nowTime
# print pastTime
# print afterTomorrowTime
# print tomorrowTime

# curTime = datetime.datetime.now()
# print curTime
# desTime = curTime.replace(hour=10, minute=10, second=0, microsecond=0)
# print desTime
# delta = desTime - curTime
# print delta
# sleeptime = delta.total_seconds()
# print "Now day must sleep %d seconds" % sleeptime
# time.sleep(sleeptime)
# print '时间到了'


i = datetime.datetime.now()
# print ("当前的日期和时间是 %s" % i)
# print ("ISO格式的日期和时间是 %s" % i.isoformat())
# print ("当前的年份是 %s" % i.year)
# print ("当前的月份是 %s" % i.month)
# print ("当前的日期是  %s" % i.day)
# print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
# print ("当前小时是 %s" % i.hour)
# print ("当前分钟是 %s" % i.minute)
# print ("当前秒是  %s" % i.second)
# print ("今天是%s年%s月%s日" % (i.year, i.month, i.day))
riqi = "%s年%s月%s日" % (i.year, i.month, i.day)
print riqi

schedule = sched.scheduler(time.time, time.sleep)

def func(string1, float1):
    print i.year, "年", i.month, "月", i.day, "日", datetime.datetime.now().hour, "点", datetime.datetime.now().minute, "分", datetime.datetime.now().second, "秒" " | output=", string1, float1


# print time.time()
# schedule.enter(2,0,func,("test1",time.time()))
# schedule.enter(2,0,func,("test1",time.time()))
# schedule.enter(3,0,func,("test1",time.time()))
# schedule.enter(4,0,func,("test1",time.time()))
# schedule.run()
# print time.time()


def printtext():
    print unicode("%s月%s日%s点%s分%s秒" % (
        datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().hour,
        datetime.datetime.now().minute, datetime.datetime.now().second) + '95598智能互动网站无异常，点击“登录”，出现升级页面。', "utf8")

for i in range(13):
    schedule.enter(10*i, 0, printtext, ())
schedule.run()
