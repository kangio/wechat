#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: yangkang
@license: Apache Licence 
@contact: ghooo55@gmail.com
@site: http://abc.com/
@software: PyCharm
@file: one.py
@time: 2017/10/20 下午5:13
"""
import re
import time

import itchat
from itchat.content import *
from answers.views import answer
# print(answer('nihao'))

#
# @itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
# def text_reply(msg):
#     print(msg['Text'])


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    reply_content=msg['Text']
    print(reply_content)
    print(msg.keys)
    print(msg)
    # if msg['Type'] == 'Text':
    #     reply_content = msg['Text']
    # elif msg['Type'] == 'Picture':
    #     reply_content = "图片: " + msg['FileName']
    # elif msg['Type'] == 'Card':
    #     reply_content = " " + msg['RecommendInfo']['NickName'] + " 的名片"
    # elif msg['Type'] == 'Map':
    #     x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1,
    #                                                                                                                 2,
    #                                                                                                                 3)
    #     if location is None:
    #         reply_content = "位置: 纬度->" + x.__str__() + " 经度->" + y.__str__()
    #     else:
    #         reply_content = "位置: " + location
    # elif msg['Type'] == 'Note':
    #     reply_content = "通知"
    # elif msg['Type'] == 'Sharing':
    #     reply_content = "分享"
    # elif msg['Type'] == 'Recording':
    #     reply_content = "语音"
    # elif msg['Type'] == 'Attachment':
    #     reply_content = "文件: " + msg['FileName']
    # elif msg['Type'] == 'Video':
    #     reply_content = "视频: " + msg['FileName']
    # else:
    #     reply_content = "消息"

    friend = itchat.search_friends(userName=msg['FromUserName'])
    # itchat.send("Friend:%s -- %s    "
    #             "Time:%s    "
    #             " Message:%s" % (friend['NickName'], friend['RemarkName'], time.ctime(), reply_content),
    #             toUserName='filehelper')
    # itchat.send("你好%s, 你在[%s]你发的消息[%s]已收到, 稍后回复,谢谢" % (friend['NickName'], time.ctime(),reply_content),
    #             toUserName=msg['FromUserName'])
    itchat.send(answer(msg['Text']),
                toUserName=msg['FromUserName'])

    # itchat.send("我已经收到你在【%s】发送的消息【%s】稍后回复。" % (time.ctime(), reply_content),toUserName=msg['FromUserName'])


itchat.auto_login()
itchat.run()


if __name__ == "__main__":
    pass