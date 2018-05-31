#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: yangkang
@license: Apache Licence 
@contact: ghooo55@gmail.com
@site: http://abc.com/
@software: PyCharm
@file: newpre.py
@time: 2017/8/1 下午11:00
"""


import codecs
with codecs.open('/Users/yangkang/PycharmProjects/smartdj/answers/cc.txt','r','utf-8') as cc:
    a=cc.readline()
    res=[]
    temp=[]
    while len(a)!=0:
        print a
        while(len(a)>2):
            temp.append(a.strip())
            a = cc.readline()
        res.append(temp)
        temp=[]
        a=cc.readline()

print 'a',res
with codecs.open('/Users/yangkang/PycharmProjects/smartdj/answers/nr.txt','r','utf-8') as cc:
    a=cc.readline()
    result=[]
    while len(a)!=0:
        while(len(a)>2):
            temp.append(a)
            a=cc.readline()
        result.append(''.join(temp))
        temp=[]
        a=cc.readline()

newmap={}

for index,i in enumerate(res):
    for j in i:
        newmap[j.upper()]=result[index]




def new_predict(text):
    if text.upper() in newmap.keys():
        print text.upper
        return newmap[text.upper()]
    else:return '小移正在成长中,暂时无法回答您的问题'






if __name__ == "__main__":
    # print new_predict(u'不想用增值业务了，样取消？')
    pass