#coding=utf-8
import re
import jieba
import jieba.posseg as posseg
from . import corpustools
from .word_dictionary import Dictionary


class CorpusSegement:
    def __init__(self):
        for i in Dictionary.usrdict:
            elem=i.split(' ')
            if len(elem)==1:
                jieba.add_word(i)
            elif len(elem)==2:
                jieba.add_word(elem[0], tag=elem[1])
            else:jieba.add_word(elem[0], tag=elem[1],freq=int(elem[2]))
        for i in Dictionary.keywords:
            elem = i.split(' ')
            if len(elem) == 1:
                jieba.add_word(i)
            elif len(elem) == 2:
                jieba.add_word(elem[0], freq=int(elem[1]))
            else:
                jieba.add_word(elem[0], freq=int(elem[1]), tag=elem[2])

        # self.stopwords=corpustools.myread('./data/newstop.txt')
        # self.actionwords=corpustools.myread('./data/action.txt')
        self.stopwords=Dictionary.newstop
        self.actionwords=Dictionary.action
        self.similardict={}
        for i in Dictionary.similar:
            j=i.split(' ')
            for m in range(1,len(j)):
                self.similardict[j[m]]=j[0]
    def single_segment(self,line,hasOrigin=True):
        lineok=corpustools.preDeal(line)
        model=list(posseg.cut(lineok,False))

        words=[i.word for i in model]
        flags=[i.flag if 'v' in i.flag or 'l' in i.flag else '' for i in model]
        result=[]
        for i in range(len(words)):
            word=words[i]
            if word in list(self.similardict.keys()):
                word=self.similardict[word]
            # if re.match(ur'\b[\d.]+\b',word) or ' ' in word:continue
            if words[i] in self.stopwords:continue
            if 'v' in flags[i] and i<len(words)-1:
                if words[i+1] in ['了','的']:

                    result.append(word)
                    continue
            # elif words[i] in self.similardict.keys():
            #     result.append(self.similardict[words[i]]+flags[i])
            result.append(word+flags[i])
        if hasOrigin==True:
            result.append('####'+line)
        return result
    def segmenter(self,corpus,hasOrigin=True,isWrite=False,name='default_seg.txt'):
        print('>>>开始分词......')
        result_list=[self.single_segment(line,hasOrigin=hasOrigin) for line in corpus]
        if isWrite:
            corpustools.mywrite(result_list,name,'short')

        return result_list


if __name__=='__main__':
    myaction = []
    b=CorpusSegement()
    from collections import defaultdict
    dd=defaultdict(int)

    # for j in b.single_segment(u'怎么??？安装的'):
    #     print j
    cor=corpustools.myread('corpus.txt',del_empty=True)
    s=b.segmenter(cor,isWrite=True,name='copy_of_linux/cor_segact_total')


    #
    #
    # cor=corpustools.myread('copy_of_linux/inner/wlan_apply',del_empty=True)
    # s=b.segmenter(cor,isWrite=False,name='copy_of_linux/inner/wlan_apply_actions')
    #
    #
    # # s=b.segmenter(cor,isWrite=True,hasOrigin=False,name='copy_of_linux/cor_segact_pure')
    # # # s=[['1v','2v'],['1v','4v']]
    # for i in s:
    #     for j in i:
    #         if j[-1] in u'vn' and '####' not in j:
    #             dd[j.strip('vn')]+=1
    #             myaction.append(j.strip('vn'))
    # words=sorted(dd.items(),key=lambda x:x[1],reverse=True)
    # wordslist=[i[0] for i in words]
    # # corpustools.mywrite(wordslist,'wordfreq')
    # corpustools.mywrite(wordslist,'copy_of_linux/inner/wlan_apply_actions')
    #



