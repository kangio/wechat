# coding=utf-8
import codecs
import sys
from .scean import *
from .word_dictionary import Dictionary

from . import corpustools
from .corpus_segment import CorpusSegement
from .chatbot_integration import tmp_a


def iscontain(line, mtup):  # mtup是一个元组，每个元素是一个list，每个list至少一个在line中
    flag = True
    for mlist in mtup:
        for i in mlist:
            if i in line:
                break
            if i == mlist[-1]:
                flag = False
                return flag

    return flag


def inaction(line, scr):
    if len(scr.action) == 0: return True
    b = line.split(" ")
    out = []
    for i in b:
        if len(i) > 0:
            # if i[-1] in u'vn' and len(i.strip('uv')) > 1: out.append(i.strip('vn'))
            if i[-1] in 'vn' and i.strip('uv') in Dictionary.newaction: out.append(i.strip('vn'))
    # global myaction
    # myaction+=out
    out = [i for i in out if i not in scr.action]
    if len(out) > 0:
        return False
    else:
        return True


def inscene(line, scr):
    if scr == None:
        return True
    flag = False
    if inscene(line, scr.BASE):
        if len(scr.rule.items) == 0:
            return True
        for tup in scr.rule.items:

            if iscontain(line, tup):
                flag = True
                break
        return flag
    return flag


def inask(line, scr):
    if len(scr.askword) == 0: return True
    out = [i for i in Dictionary.askword if i in line and i not in scr.askword]
    if len(out) > 0:
        return False
    return True


def outbad(line, scr):
    if len(scr.bad) == 0: return True
    out = [i for i in scr.bad if i in line]
    if len(out) > 0: return False
    return True


def getv(line):
    pp = '------'
    s = line.split(' ')
    for i in s:
        if len(i) > 0:
            if i[-1] in 'vn' and len(i.strip('uv')) > 1: pp += i + ' | '
    return pp


# b=CorpusSegement()
# cor=corpustools.myread('../corpus.txt',del_empty=True)
# b.segmenter(cor,isWrite=True,name='cor_seg.txt')
filepath = 'cor_segact_total'


# filepath='cor_seg.txt'

def sdeal(sc, name='defaultresult'):
    out = []
    rest = []
    total=[]

    # global myaction
    # myaction=[]

    ##########################################################################
    # sc = llzytc  # 带分析场景
    ##########################################################################
    # line=u'怎么 销户 不 清零v ####怎么停机不清零'
    # dl = line.split('####')
    # if inscene(dl[0], sc):
    #     print 'ok'
    #     # out.append(dl[1].strip() + getv(dl[0]))
    #     if inask(dl[0], sc):
    #         if inaction(dl[0], sc):
    #             out.append(dl[1].strip() + getv(dl[0]))
    #         else:
    #             rest.append(dl[1].strip() + getv(dl[0]))
    #     else:
    #         print line
    #     if len(out)>0:print 'out:',out[0]
    #     if len(rest)>0:print 'rest',rest[0]

    with codecs.open(filepath, 'r', 'utf-8') as cc:
        line = cc.readline()


        while line != '':
            dl = line.split('####')
            if inscene(dl[0], sc):
                # out.append(dl[1].strip() + getv(dl[0]))
                if inask(dl[0], sc):
                    if inaction(dl[0], sc):
                        if outbad(dl[0], sc):
                            out.append(dl[1].strip())
                        else:
                            print('badword--', line)
                    else:
                        rest.append(dl[1].strip() + getv(dl[0]))
                else:
                    print(line)
                    # out.append(dl[1].strip() + getv(dl[0]))

            line = cc.readline()

    corpustools.mywrite(list(set(out)), 'inner/' + name)
    corpustools.mywrite(list(set(rest)), 'inner/' + name + '_left')

    # corpustools.mywrite(list(set(myaction)), name + '_action')


if __name__ == '__main__':
    # for i in range(len(scenelib)):
    #     sdeal(scenelib[i],scenelibname[i])
    # sdeal(jf,'jifenxingji')
    sdeal(wfsy, nm[wfsy])
    # sdeal(aabbcc,'test')
    # i=12
    # sdeal(scenelib[i], scenelibname[i])


