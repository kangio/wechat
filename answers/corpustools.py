#coding=utf-8
import codecs
import re
import random
from collections import defaultdict
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

def preDeal(line):
    line=line.upper()
    line=re.sub('4G','四代',line)
    line=re.sub('帐','账',line)
    line=re.sub('不$','吗',line)
    line=re.sub('的$','',line)
    line=re.sub('的[。，！？]',' ',line)
    line=re.sub('不怎么','不',line)
    co = re.compile(r'[,.!@#，。！?？:;：；￥%…&*]')
    line=re.sub(co,' ',line)
    line=re.sub(r'不(?=^\u4e00-\u9fa5)','吗',line)
    if re.search(r'(你|)可以帮我(.*?)吗',line):
        line=re.sub(r'(你|)可以帮我(.*)吗',re.search(r'(你|)可以帮我(.*?)吗',line).group(2),line)
    if re.search(r'(你|)可以帮我(.*?)嘛',line):
        line=re.sub(r'(你|)可以帮我(.*)嘛',re.search(r'(你|)可以帮我(.*?)嘛',line).group(2),line)
    if re.search(r'(你|)能(查询一下|查一下|帮我)(.*?)吗', line):
        line = re.sub(r'(你|)能(查询一下|查一下|帮我)(.*?)吗', re.search(r'(你|)能(查询一下|查一下|帮我)(.*?)吗', line).group(3), line)
    if re.search(r'把(.*)了', line):
        line = re.sub(r'把(.*)了', re.search(r'把(.*)了', line).group(1), line)
    pattern0=re.compile(r'(请问你一下|我想咨询一下|咨询一下|帮我查一下|我想问一下|请问一下|我想查一下|想问一下|我想问下|我想问问|我想问|问一下|问下|问你下|请帮我|不好意思|帮我|我想|请问|您好|你好)')
    line=re.sub(pattern0,'',line)

    pattern1 = re.compile(
        r'[\d一二三四五六七八九十百]+(圆|元|块钱|块|)[\d一二三四五六七八九十]?([的档包买])([\d一二三四五六七八九十百]*)(个|)(分钟|分|小时)(的|)(套餐|)', re.I)
    line = re.sub(pattern1, '时长', line)
    pattern1 = re.compile(
        r'[\d一二三四五六七八九十百]+(圆|元|块钱|块|)[\d一二三四五六七八九十]?([档包])([\d一二三四五六七八九十百]*)(个|)(GB|G|MB|M|兆|多兆)(的|)(通用流量包|套餐流量|流量套餐|流量包|安心包|流量|加油包|快餐包|)', re.I)
    line = re.sub(pattern1, '香蕉', line)
    pattern1 = re.compile(
        r'[\d一二三四五六七八九十百]+(圆|元|块钱|块|)[\d一二三四五六七八九十]?([档包])([\d一二三四五六七八九十百]*)(个|)(GB|G|MB|M|兆|多兆)(的|)(通用流量包|套餐流量|流量套餐|流量包|安心包|流量|加油包|快餐包|)',
        re.I)
    line = re.sub(pattern1, '香蕉', line)
    pattern1 = re.compile(
        r'[\d一二三四五六七八九十百]+(圆|元|块钱|块|)[\d一二三四五六七八九十]?(档|包|的|买|)([\d一二三四五六七八九十百]*)(个|)(GB|G|MB|M|兆|多兆)(的|)(通用流量包|套餐流量|流量套餐|流量包|安心包|流量|加油包|快餐包|)',
        re.I)
    line = re.sub(pattern1, '香蕉', line)
    pattern1 = re.compile(
        r'[\d一二三四五六七八九十百]+(圆|元|块钱|块|)[\d一二三四五六七八九十]?(档|包|的|买|)([\d一二三四五六七八九十百]*)(个|)(GB|G|MB|M|兆|多兆)(的|)(通用流量包|套餐流量|流量套餐|流量包|安心包|流量|加油包|快餐包)',
        re.I)
    line = re.sub(pattern1, '香蕉', line)
    line=re.sub('[\d年]{0,5}[\d一二三四五六七八九十]{1,2}月[\d一二三四五六七八九十]{1,3}日？曰？号？','时辰',line)
    line=re.sub('[\d一二三四五六七八九十百几]{1,6}(元|多块钱|多块|块多|块|毛|毛钱)','元宝',line)
    line=re.sub('[\d一二三四五六七八九十百几]{1,6}(多兆|兆多|M)','果酱',line)
    line=re.sub('^[^\w\u4e00-\u9fa5]*','',line)
    return line

def myread(name,del_empty=False):
    with codecs.open(name,'r','utf-8') as source:
        ans=source.readlines()
    ans=[i.strip() for i in ans]
    if del_empty==True:
        ans=[i for i in ans if len(i)>0]
    return ans

def mywrite(mylist,name,mode='long'):
    source=codecs.open(name,'w','utf-8')
    if len(mylist)==0:
        # print "nothing to write!"
        source.write('')
        source.close()
        logging.warn("nothing to write.")
        return
    if type(mylist[0])==str or type(mylist[0])==str:
        for i in mylist:
            source.write(i+'\n')
    elif type(mylist[0])==list:
        if mode=='short':
            for i in mylist:
                source.write(' '.join(i)+'\n')
        elif mode=='long':
            for i in mylist:
                for j in i:
                    source.write(j+'\n')
                source.write('\n\n\n\n')
    source.close()

def pprint(mlist,mode='long'):
    if len(mlist)==0:
        print('nothing!')
        return
    if type(mlist[0])==str or type(mlist[0])==str:
        print(' '.join(mlist))
    elif type(mlist[0][0])==str:
        if mode=='short':
            for i in mlist:
                print('|'.join(i))
        else:
            for i in mlist:
                for j in i:
                    print(j)
                print('\n\n')
    elif type(mlist[0][0])==list:
        pprint([[' '.join(j) for j in i] for i in mlist],mode)

def word_bags(cut_corpus_list):
    freq=defaultdict(int)
    for sub_line_list in cut_corpus_list:
        for token in list(set(sub_line_list)):
            freq[token]+=1
    return freq

def load_config(path):
    s=myread(path,del_empty=True)
    freq={}
    for i in s:
        if i[0]=='#':continue
        p=i.split('=')
        freq[p[0].lower()]=p[1].lower()
    return freq

def clusterRead(name):
    txt=myread(name)
    txt=[i.split('####')[1] if '####' in i else i for i in txt]
    out=[]
    newpart=[]
    key=True
    for i in txt:
        if len(i)==0:
            if key==False:
                if '(' in newpart[0] or '---' in newpart[0]:
                    newpart=newpart[1:]
                out.append(newpart)
            key=True
            continue
        if key==True:
            newpart=[]
            key=False
        newpart.append(i)
    print('读取文件名为：%s，类数为：%d'%(name,len(out)))
    return out

def corpus_choose_randomly(name, num):
    txt=myread(name)
    # pprint(txt)
    if num>len(txt):
        return
    a=random.sample(txt,num)
    return a

def clean_corpus(mlist,sentence_lengh=2):
    # mlist=[preDeal(i) for i in mlist]

    s=[i for i in mlist if len(preDeal(i))>sentence_lengh]
    s=list(set(s))
    print('原始传入语料%d条，抽取用于聚类的问句%d条'%(len(mlist),len(s)))
    # mywrite(s, 'output/corpusOn')
    # mywrite([i for i in mlist if i not in s], 'output/corpusOff')
    return s

import time
class timer:
    def __init__(self):
        self.begin=time.time()
    def click(self):
        now=time.time()
        print('花费时间为：',now-self.begin)
        self.begin=now







