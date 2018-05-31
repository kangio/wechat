#encoding=utf-8
import sys as O0O0OOO0O00O0O00O #line:1
import jieba as OO000OOO0O0O0OOO0 #line:2
import jieba .posseg as O0O0O00O00000OO0O #line:3
import datetime as OOO0OOOO00OO0OOO0 #line:4
import re as OOOOO0OOOO0O0OO00 #line:5
import time as OO0O000O000O00000 #line:6
import logging as OO0O0OO00O0O0O0O0 #line:7
def and_condition (O0OO000OOOO00OOOO ):#line:12
    pass #line:13
def or_condition (OOO0000000O0O0O0O ,O000000OO0OO00O0O ):#line:15
    pass #line:16
def only_condition (OOO00O000000OOOOO ):#line:18
    pass #line:19
def reject_condition (OO000OOOOO0O00OOO ):#line:21
    pass #line:22
class tmp_a :#line:25
    def __init__ (O0OO00OO00OO0OOO0 ):#line:26
        O0OO00OO00OO0OOO0 .zt =["不能","无法","没法","不足","不了","不够","不多","欠费"]#line:27
        O0OO00OO00OO0OOO0 .zt1 =["欠费了","不够了","不足了","停机了"]#line:28
        O0OO00OO00OO0OOO0 .noaccount_needadd1 =["充值了","充了","充钱了","冲了","交了","充过"]#line:30
        O0OO00OO00OO0OOO0 .noaccount_needadd2 =["不能","无法","没法","不足","不了"]#line:31
        O0OO00OO00OO0OOO0 .noaccount_keywords_1 =["充","充值了","充了","冲","冲了","交了","充值","缴费","交费","充话费","交","充过"]#line:32
        O0OO00OO00OO0OOO0 .noaccount_keywords =["没显示","没有显示","没反应","没有反应","没有收到","没收到","没增加","没有增加","没提示","没有提示" "停机","打不出去","还不通","还欠费","没到","没有到","欠费","欠","停机","不能","无法","没法","没变","没钱"]#line:34
        O0OO00OO00OO0OOO0 .noaccount_keywords_2 =["没到账","没有到账","没给充上","没有充上","不到账","未到账","不进账"]#line:35
        O0OO00OO00OO0OOO0 .nook_keyword2 =["有","还有"]#line:37
        O0OO00OO00OO0OOO0 .nook_keyword3 =["钱","余额","元"]#line:38
        O0OO00OO00OO0OOO0 .nook_keyword =["只到了","只到账","不对","只有","只剩","只","少了","不准确","就剩","怎么剩","就还剩","应该还剩","不一致","不一样","对不上","打不出去","打不通","不能","无法","没法","有问题","有点问题"]#line:41
        O0OO00OO00OO0OOO0 .nook_keyword1 =["话费","余额","查话费"]#line:42
        O0OO00OO00OO0OOO0 .noaccount_exceptwords =["兑换","流量","积分","宽带","星级","游戏","电子券","活动","发票","充错","会员","打印发票","送"]#line:44
        O0OO00OO00OO0OOO0 .noaccount_keywords_3 =["微信公众号","公众号","app","客户端","掌厅","掌上营业厅"]#line:45
        O0OO00OO00OO0OOO0 .huafei_1 =["充","交","冲","冲话费","充流量","充话费","充值","充钱","缴费"]#line:47
        O0OO00OO00OO0OOO0 .huafei_2 =["方法","哪里","怎么","方式","如何","渠道","我想","我要","想","要","咋","怎样"]#line:48
        O0OO00OO00OO0OOO0 .huafei_3 =["发票","开发票","q","qb","qq币","qq","打印发票","记录","电费","座机","固定电话","会员","扣币"]#line:49
        O0OO00OO00OO0OOO0 .huafei_4 =["刚","刚刚","积分","宽带","星级","游戏","电子券","活动","兑换","固话","开机","漫游","语音","扣","账单","明细","详单"]#line:50
        O0OO00OO00OO0OOO0 .huafei_5 =["知道","了解"]#line:51
        O0OO00OO00OO0OOO0 .yue_1 =["查","查询"]#line:53
        O0OO00OO00OO0OOO0 .yue_2 =["话费","钱","余额"]#line:54
        O0OO00OO00OO0OOO0 .yue_3 =["剩","剩余","有多少","还有多少"]#line:55
        O0OO00OO00OO0OOO0 .yue_4 =["查话费","余额"]#line:56
        O0OO00OO00OO0OOO0 .tkz =OO000OOO0O0O0OOO0 .Tokenizer ()#line:58
        from .word_dictionary import Dictionary as O00OO0O0O0O000OOO #line:59
        for O00000O00OO00O000 in O00OO0O0O0O000OOO .meword :#line:60
            O0O00OO0OOOO0OOO0 =O00000O00OO00O000 .split (' ')#line:61
            if len (O0O00OO0OOOO0OOO0 )==1 :#line:62
                O0OO00OO00OO0OOO0 .tkz .add_word (O00000O00OO00O000 )#line:63
            elif len (O0O00OO0OOOO0OOO0 )==2 :#line:64
                O0OO00OO00OO0OOO0 .tkz .add_word (O0O00OO0OOOO0OOO0 [0 ],tag =O0O00OO0OOOO0OOO0 [1 ])#line:65
            else :#line:66
                O0OO00OO00OO0OOO0 .tkz .add_word (O0O00OO0OOOO0OOO0 [0 ],tag =O0O00OO0OOOO0OOO0 [2 ],freq =int (O0O00OO0OOOO0OOO0 [1 ]))#line:67
        O0OO00OO00OO0OOO0 .psegp =O0O0O00O00000OO0O .POSTokenizer (O0OO00OO00OO0OOO0 .tkz )#line:69
    def process_charge (OOO000OO0000O0O0O ,O0OOO0O00O0O00000 ,OOO000O000O0OOO00 ):#line:71
        O0OOO0O00O0O00000 =O0OOO0O00O0O00000 .replace ("帐","账")#line:72
        O0OOO0O00O0O00000 =O0OOO0O00O0O00000 .lower ()#line:73
        O0O00OO0O0O0O00O0 =OOO000OO0000O0O0O .psegp .cut (O0OOO0O00O0O00000 )#line:75
        OOOO0O0OO000O0O0O =0 #line:76
        O00OO00O00OO00000 =False #line:78
        OOO0O0O0OOOO0O00O =False #line:79
        OO0000OOOOOO000O0 =False #line:80
        O000000O0000OO00O =False #line:81
        O0OO00OOOO00O0000 =False #line:82
        O0O00O00OOOO00000 =False #line:83
        OO0O0O0O00O0O0000 =False #line:84
        OOOOO000OOO00OO00 =False #line:85
        O0OOOOO000OOOO0OO =False #line:86
        O0OOOO0000OOOO0OO =False #line:87
        OO0O0O0000OOOO0OO =False #line:88
        OO00OOOO0OOOO00OO =False #line:90
        OO0O0OO0OO0O0OO0O =False #line:91
        O0O000O00O00O000O =False #line:92
        OO0OOOOO00OOO00O0 =False #line:93
        O0OO00000OOOO0OO0 =False #line:94
        O0OOO00000OO0OO00 =False #line:95
        O0OOO0OOOO0O0OO0O =False #line:96
        OO00OO0O00OOO00O0 =False #line:97
        O0O0O000OO0OOO0OO =False #line:99
        OO00OOOO000O0000O =False #line:100
        O00OOO00O0O000000 =False #line:102
        O00OO00O0OO0O0000 =False #line:103
        O0000OOOO0O00O0O0 =False #line:104
        OO0OOOOO0OO0O0O0O =False #line:105
        OOO0OOO00OOO0O00O =False #line:107
        O00OO00OOOOO0O0O0 =[]#line:109
        OOOO0OO0OOO00OOO0 =[]#line:110
        for OO00O0000OOO0O000 ,O00O0OO0000O00OO0 in O0O00OO0O0O0O00O0 :#line:111
            OOOO0O0OO000O0O0O +=1 #line:114
            if (O00O0OO0000O00OO0 =="x"):#line:116
                O00OO00OOOOO0O0O0 .append (OOOO0OO0OOO00OOO0 )#line:117
                OOOO0OO0OOO00OOO0 =[]#line:118
                if not (OOO0O0O0OOOO0O00O and OO0000OOOOOO000O0 ):#line:119
                    OOO0O0O0OOOO0O00O =False #line:120
                    OO0000OOOOOO000O0 =False #line:121
            else :#line:122
                OOOO0OO0OOO00OOO0 .append ((OO00O0000OOO0O000 ,O00O0OO0000O00OO0 ))#line:123
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_1 ):OOO0O0O0OOOO0O00O =True #line:125
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_2 ):OO0000OOOOOO000O0 =True #line:126
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_3 ):O000000O0000OO00O =True #line:127
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_4 ):O0OOO00000OO0OO00 =True #line:128
            if (O00O0OO0000O00OO0 =="v"and OO00O0000OOO0O000 not in OOO000OO0000O0O0O .huafei_1 and OO00O0000OOO0O000 not in OOO000OO0000O0O0O .huafei_5 ):#line:129
                O000000O0000OO00O =True #line:130
            if (O00O0OO0000O00OO0 =="zt"or O00O0OO0000O00OO0 =="qd"):#line:131
                O000000O0000OO00O =True #line:132
            if (O00O0OO0000O00OO0 =="x"and ((OOO0O0O0OOOO0O00O ==True and OO0000OOOOOO000O0 ==False )or (OOO0O0O0OOOO0O00O ==False and OO0000OOOOOO000O0 ==True ))):#line:133
                O000000O0000OO00O =True #line:134
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .yue_1 ):OO00OOOO0OOOO00OO =True #line:136
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .yue_2 ):OO0O0OO0OO0O0OO0O =True #line:137
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .yue_3 ):O0O000O00O00O000O =True #line:138
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .yue_4 ):OO0OOOOO00OOO00O0 =True #line:139
            if (O00O0OO0000O00OO0 =="zq"):O0OO00000OOOO0OO0 =True #line:140
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .noaccount_keywords_2 ):OO0O0O0000OOOO0OO =True #line:142
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .nook_keyword ):O0OOOO0000OOOO0OO =True #line:143
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .nook_keyword1 ):OO00OO0O00OOO00O0 =True #line:144
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .noaccount_keywords_1 ):O0OOOOO000OOOO0OO =True #line:145
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .noaccount_keywords ):O0OO00OOOO00O0000 =True #line:146
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .noaccount_exceptwords ):O0O00O00OOOO00000 =True #line:147
            if (OO00O0000OOO0O000 =="10086"):OO0O0O0O00O0O0000 =True #line:148
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .noaccount_keywords_3 ):O0OOO0OOOO0O0OO0O =True #line:149
            if (OO00O0000OOO0O000 in ["微信","支付宝"]):OOOOO000OOO00OO00 =True #line:150
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .noaccount_needadd1 ):O0O0O000OO0OOO0OO =True #line:152
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .noaccount_needadd2 ):OO00OOOO000O0000O =True #line:153
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .zt ):O00OOO00O0O000000 =True #line:155
            if (OOO0O0O0OOOO0O00O and OO0000OOOOOO000O0 and O00OOO00O0O000000 ==False ):O00OO00O0OO0O0000 =True #line:156
            if (OOO0O0O0OOOO0O00O ==False and OO0000OOOOOO000O0 ==False and O00OOO00O0O000000 ):O0000OOOO0O00O0O0 =True #line:157
            if (OOO0O0O0OOOO0O00O and OO0000OOOOOO000O0 and O0000OOOO0O00O0O0 ):OO0OOOOO0OO0O0O0O =True #line:158
            if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .zt1 ):OOO0OOO00OOO0O00O =True #line:160
        if len (OOOO0OO0OOO00OOO0 )>0 :O00OO00OOOOO0O0O0 .append (OOOO0OO0OOO00OOO0 )#line:162
        if (O0O00O00OOOO00000 ==False and OOO0OOO00OOO0O00O ==False ):#line:165
            if (OO0O0O0000OOOO0OO or (O0OO00OOOO00O0000 and O0OOOOO000OOOO0OO )or (O0O0O000OO0OOO0OO and OO00OOOO000O0000O )):#line:166
                if (OO0O0O0O00O0O0000 and O0OOO0OOOO0O0OO0O ):OOO000O000O0OOO00 .append ("noaccount_10086")#line:167
                elif (OOOOO000OOO00OO00 ):OOO000O000O0OOO00 .append ("noaccount_weixin")#line:168
                else :OOO000O000O0OOO00 .append ("noaccount")#line:169
                O00OO00O00OO00000 =True #line:170
        if (O0OOOO0000OOOO0OO and (O0OOOOO000OOOO0OO or OO00OO0O00OOO00O0 )and O0O00O00OOOO00000 ==False and O00OO00O0OO0O0000 ==False and OO0OOOOO0OO0O0O0O ==False ):#line:173
            OOO000O000O0OOO00 .append ("balance_nocorrect")#line:174
            O00OO00O00OO00000 =True #line:175
        if (O00OO00O00OO00000 ==False and O0O0O000OO0OOO0OO ==False and OO0O0O0000OOOO0OO ==False and O000000O0000OO00O ==False and O0OOO00000OO0OO00 ==False and OOO0O0O0OOOO0O00O and OO0000OOOOOO000O0 ):#line:178
            OOO000O000O0OOO00 .append ("rechagre_method")#line:179
            O00OO00O00OO00000 =True #line:180
        if (OOO0O0O0OOOO0O00O and OOOO0O0OO000O0O0O ==1 ):#line:182
            OOO000O000O0OOO00 .append ("rechagre_method")#line:183
            O00OO00O00OO00000 =True #line:184
        if (O00OO00O00OO00000 ==False and O0O0O000OO0OOO0OO ==False and OO0O0O0000OOOO0OO ==False ):#line:186
            for O0OO000O0000OOOOO in O00OO00OOOOO0O0O0 :#line:187
                OOO0O0O0OOOO0O00O =False #line:188
                OO0000OOOOOO000O0 =False #line:189
                O000000O0000OO00O =False #line:190
                O0OOO00000OO0OO00 =False #line:191
                for OO00O0000OOO0O000 ,O00O0OO0000O00OO0 in O0OO000O0000OOOOO :#line:192
                    if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_1 ):OOO0O0O0OOOO0O00O =True #line:193
                    if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_2 ):OO0000OOOOOO000O0 =True #line:194
                    if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_3 ):O000000O0000OO00O =True #line:195
                    if (OO00O0000OOO0O000 in OOO000OO0000O0O0O .huafei_4 ):O0OOO00000OO0OO00 =True #line:196
                    if (O00O0OO0000O00OO0 =="v"and OO00O0000OOO0O000 not in OOO000OO0000O0O0O .huafei_1 and OO00O0000OOO0O000 not in OOO000OO0000O0O0O .huafei_5 ):O000000O0000OO00O =True #line:197
                if (O000000O0000OO00O ==False and O0OOO00000OO0OO00 ==False and OOO0O0O0OOOO0O00O and OO0000OOOOOO000O0 ):#line:199
                    OOO000O000O0OOO00 .append ("rechagre_method")#line:200
                    O00OO00O00OO00000 =True #line:201
                    break #line:202
        if (O00OO00O00OO00000 ==False and O0OO00000OOOO0OO0 ==False and O0O00O00OOOO00000 ==False and O0OOO00000OO0OO00 ==False ):#line:205
            if (((OO00OOOO0OOOO00OO or O0O000O00O00O000O )and OO0O0OO0OO0O0OO0O )or (OO0000OOOOOO000O0 and OO0OOOOO00OOO00O0 )):#line:206
                OOO000O000O0OOO00 .append ("balance_search")#line:207
                O00OO00O00OO00000 =True #line:208
            if (OO0OOOOO00OOO00O0 and OOOO0O0OO000O0O0O ==1 ):#line:210
                OOO000O000O0OOO00 .append ("balance_search")#line:211
                O00OO00O00OO00000 =True #line:212
    def process_password (OO0OO000OO00O0000 ,O0O0OO0OO0OO0OO0O ,O0O0OOO0OO00OOOOO ):#line:216
        if (O0O0OO0OO0OO0OO0O .find ("密码")>=0 or O0O0OO0OO0OO0OO0O .find ("蜜码")>=0 ):#line:217
            if (O0O0OO0OO0OO0OO0O .find ("服务")>=0 or O0O0OO0OO0OO0OO0O .find ("客服")>=0 ):#line:218
                if (O0O0OO0OO0OO0OO0O .find ("忘")>=0 or O0O0OO0OO0OO0OO0O .find ("记")>=0 or O0O0OO0OO0OO0OO0O .find ("找回")>=0 or O0O0OO0OO0OO0OO0O .find ("不知道")>=0 or O0O0OO0OO0OO0OO0O .find ("找到")>=0 or O0O0OO0OO0OO0OO0O .find ("不对")>=0 ):#line:220
                    O0O0OOO0OO00OOOOO .append ("password_retrieve")#line:221
                elif (O0O0OO0OO0OO0OO0O .find ("改")>=0 or O0O0OO0OO0OO0OO0O .find ("更换")>=0 or O0O0OO0OO0OO0OO0O .find ("重置")>=0 or O0O0OO0OO0OO0OO0O .find ("重设")>=0 or O0O0OO0OO0OO0OO0O .find ("重新设")>=0 or O0O0OO0OO0OO0OO0O .find ("盗")>=0 or O0O0OO0OO0OO0OO0O .find ("泄露")>=0 ):#line:223
                    O0O0OOO0OO00OOOOO .append ("password_reset")#line:224
                elif ((O0O0OO0OO0OO0OO0O .find ("是什么")>=0 or O0O0OO0OO0OO0OO0O .find ("什么是")>=0 or O0O0OO0OO0OO0OO0O .find ("介绍")>=0 or O0O0OO0OO0OO0OO0O .find ("啥叫")>=0 or O0O0OO0OO0OO0OO0O .find ("是啥")>=0 or O0O0OO0OO0OO0OO0O .find ("意思")>=0 or O0O0OO0OO0OO0OO0O .find ("用来")>=0 or O0O0OO0OO0OO0OO0O .find ("获取")>=0 )and O0O0OO0OO0OO0OO0O .find ("不")<0 and O0O0OO0OO0OO0OO0O .find ("锁")<0 ):#line:228
                    O0O0OOO0OO00OOOOO .append ("password_intro")#line:229
                elif (O0O0OO0OO0OO0OO0O .find ("查")>=0 or O0O0OO0OO0OO0OO0O .find ("多少")>=0 ):#line:230
                    O0O0OOO0OO00OOOOO .append ("password_search")#line:231
    def process_addedservice (OO00O0OOO00O000OO ,O00000O000000O00O ,O0OO00OO000OO0000 ):#line:233
        if (O00000O000000O00O .find ("增值业务")>=0 or O00000O000000O00O .find ("增值服务")>=0 ):#line:234
            if (O00000O000000O00O .find ("影响")<0 and O00000O000000O00O .find ("为什么")<0 ):#line:235
                if ((O00000O000000O00O .find ("取消")>=0 or O00000O000000O00O .find ("关")>=0 or O00000O000000O00O .find ("退")>=0 or O00000O000000O00O .find ("停")>=0 or O00000O000000O00O .find ("删")>=0 or O00000O000000O00O .find ("撤")>=0 or O00000O000000O00O .find ("解除")>=0 or O00000O000000O00O .find ("消除")>=0 or O00000O000000O00O .find ("去除")>=0 )and ((O00000O000000O00O .find ("不")<0 and O00000O000000O00O .find ("有没有")<0 )or O00000O000000O00O .find ("可不可以")>=0 or O00000O000000O00O .find ("不要")>=0 or O00000O000000O00O .find ("不需要")>=0 or O00000O000000O00O .find ("不想")>=0 )):#line:240
                    O0OO00OO000OO0000 .append ("addedservice_close")#line:241
                elif (O00000O000000O00O .find ("查")>=0 or O00000O000000O00O .find ("看")>=0 or O00000O000000O00O .find ("哪些")>=0 or O00000O000000O00O .find ("有什么")>=0 or O00000O000000O00O .find ("什么增值业务")>=0 or O00000O000000O00O .find ("有没有")>=0 ):#line:243
                    O0OO00OO000OO0000 .append ("addedservice_search")#line:244
    def process_bill (OO0000OOO0O000OO0 ,O0O00O0000OOOOOO0 ,OOO0O0O0OOO000OOO ):#line:246
        O00000O0O0OOO00OO =OOOOO0OOOO0O0OO00 .compile ("(账单|帐单|明细|话单|详单|详情|((通话|通讯|电话|话费|消费)(记录|纪录)))$")#line:247
        if (O0O00O0000OOOOOO0 .find ("账单")>=0 or O0O00O0000OOOOOO0 .find ("记录")>=0 or O0O00O0000OOOOOO0 .find ("帐单")>=0 or O0O00O0000OOOOOO0 .find ("纪录")>=0 or O0O00O0000OOOOOO0 .find ("明细")>=0 or O0O00O0000OOOOOO0 .find ("详单")>=0 or O0O00O0000OOOOOO0 .find ("话单")>=0 ):#line:250
            O00O0OOO000OO0OOO =False #line:251
            O0O00000OOO00OOO0 =False #line:252
            O00OOO000O00O00O0 =False #line:253
            if (O0O00O0000OOOOOO0 .find ("发票")<0 and O0O00O0000OOOOOO0 .find ("打印")<0 and O0O00O0000OOOOOO0 .find ("下载")<0 and O0O00O0000OOOOOO0 .find ("139邮箱")<0 and O0O00O0000OOOOOO0 .find ("密码")<0 and O0O00O0000OOOOOO0 .find ("139信箱")<0 ):#line:256
                O00000000OO00O0OO =O00000O0O0OOO00OO .search (O0O00O0000OOOOOO0 )#line:257
                if ((O0O00O0000OOOOOO0 .find ("查")>=0 or O0O00O0000OOOOOO0 .find ("看")>=0 or O0O00O0000OOOOOO0 .find ("获取")>=0 )and (((O0O00O0000OOOOOO0 .find ("通话")>=0 or O0O00O0000OOOOOO0 .find ("话费")>=0 or O0O00O0000OOOOOO0 .find ("通信")>=0 or O0O00O0000OOOOOO0 .find ("消费")>=0 or O0O00O0000OOOOOO0 .find ("费用")>=0 or O0O00O0000OOOOOO0 .find ("电话")>=0 )and (O0O00O0000OOOOOO0 .find ("记录")>=0 or O0O00O0000OOOOOO0 .find ("纪录")>=0 or O0O00O0000OOOOOO0 .find ("明细")>=0 ))or (O0O00O0000OOOOOO0 .find ("账单")>=0 or O0O00O0000OOOOOO0 .find ("帐单")>=0 or O0O00O0000OOOOOO0 .find ("详单")>=0 or O0O00O0000OOOOOO0 .find ("话单")>=0 ))and (O0O00O0000OOOOOO0 .find ("为什么")<0 and O0O00O0000OOOOOO0 .find ("充值")<0 )):#line:263
                    OOO0O0O0OOO000OOO .append ("bill_search")#line:264
                    O00O0OOO000OO0OOO =True #line:265
                elif (O00000000OO00O0OO ):#line:266
                    OOO0O0O0OOO000OOO .append ("bill_search")#line:267
                    O00O0OOO000OO0OOO =True #line:268
                if (O00O0OOO000OO0OOO ==False ):#line:270
                    if ((((O0O00O0000OOOOOO0 .find ("通话")>=0 or O0O00O0000OOOOOO0 .find ("话费")>=0 or O0O00O0000OOOOOO0 .find ("通信")>=0 or O0O00O0000OOOOOO0 .find ("消费")>=0 or O0O00O0000OOOOOO0 .find ("费用")>=0 )and (O0O00O0000OOOOOO0 .find ("明细")>=0 ))or (O0O00O0000OOOOOO0 .find ("账单")>=0 or O0O00O0000OOOOOO0 .find ("帐单")>=0 or O0O00O0000OOOOOO0 .find ("详单")>=0 ))and (O0O00O0000OOOOOO0 .find ("有误")>=0 or O0O00O0000OOOOOO0 .find ("有问题")>=0 or O0O00O0000OOOOOO0 .find ("有错")>=0 or O0O00O0000OOOOOO0 .find ("多了")>=0 or O0O00O0000OOOOOO0 .find ("多出")>=0 or O0O00O0000OOOOOO0 .find ("多扣")>=0 or O0O00O0000OOOOOO0 .find ("不对")>=0 or O0O00O0000OOOOOO0 .find ("错误")>=0 or O0O00O0000OOOOOO0 .find ("错了")>=0 or O0O00O0000OOOOOO0 .find ("不正确")>=0 or O0O00O0000OOOOOO0 .find ("不准确")>=0 or O0O00O0000OOOOOO0 .find ("有点问题")>=0 or O0O00O0000OOOOOO0 .find ("异常")>=0 or O0O00O0000OOOOOO0 .find ("少了")>=0 or O0O00O0000OOOOOO0 .find ("这么多")>=0 )):#line:278
                        OOO0O0O0OOO000OOO .append ("bill_error")#line:279
                        O0O00000OOO00OOO0 =True #line:280
                    if (O0O00000OOO00OOO0 ==False ):#line:282
                        if (O0O00O0000OOOOOO0 .find ("没显示")>=0 or O0O00O0000OOOOOO0 .find ("没有显示")>=0 or O0O00O0000OOOOOO0 .find ("不完整")>=0 or O0O00O0000OOOOOO0 .find ("一部分")>=0 or O0O00O0000OOOOOO0 .find ("不全")>=0 or O0O00O0000OOOOOO0 .find ("没有记录")>=0 or O0O00O0000OOOOOO0 .find ("没记录")>=0 ):#line:284
                            OOO0O0O0OOO000OOO .append ("bill_incomplete")#line:285
    def predict (O00O000O0O000O000 ,OO000OOOOO00000OO ,OO0O000OO0O00OOOO ):#line:287
        # reload (O0O0OOO0O00O0O00O )#line:288
        # O0O0OOO0O00O0O00O .setdefaultencoding ('utf8')#line:289
        OO0OO000O00OOOOOO =[]#line:291
        O00O000O0O000O000 .process_charge (OO000OOOOO00000OO ,OO0OO000O00OOOOOO )#line:292
        O00O000O0O000O000 .process_password (OO000OOOOO00000OO ,OO0OO000O00OOOOOO )#line:293
        O00O000O0O000O000 .process_addedservice (OO000OOOOO00000OO ,OO0OO000O00OOOOOO )#line:294
        O00O000O0O000O000 .process_bill (OO000OOOOO00000OO ,OO0OO000O00OOOOOO )#line:295
        for OOOOO000O00O0000O in OO0OO000O00OOOOOO :#line:297
            if (OOOOO000O00O0000O =="noaccount_10086"):OO0O000OO0O00OOOO .append ("10086客户端、10086微信公众号充值未到账:\n您好，若出现您的支付账户已经扣款成功，但手机账户未查询到充值记录的情况，可能是由于银联方或其他支付方转账耗时产生延误，或某时段充值用户较多，系统繁忙等原因。建议您耐心等待，您也可以核对一下充值号码是否准确。")#line:298
            if (OOOOO000O00O0000O =="noaccount_weixin"):OO0O000OO0O00OOOO .append ("微信支付、支付宝充值未到账：\n您可以通过发送短信“CXYE”到10086，查询自己的话费是否有增加，如增加，且与充值的金额一致，那则表示充值正常。若话费没有增加，可使用腾讯官方微信号“手机充值”（微信号：wxhuafei）点击底部菜单--客户服务--订单查询与投诉，进行申诉。也可登陆淘宝或支付宝，进入“我的订单--联系客服”，进行订单情况咨询及投诉。")#line:299
            if (OOOOO000O00O0000O =="noaccount"):#line:300
                OO0O000OO0O00OOOO .append ("10086客户端、10086微信公众号充值未到账:\n您好，若出现您的支付账户已经扣款成功，但手机账户未查询到充值记录的情况，可能是由于银联方或其他支付方转账耗时产生延误，或某时段充值用户较多，系统繁忙等原因。建议您耐心等待，您也可以核对一下充值号码是否准确。\n" "微信支付、支付宝充值未到账：\n您可以通过发送短信“CXYE”到10086，查询自己的话费是否有增加，如增加，且与充值的金额一致，那则表示充值正常。若话费没有增加，可使用腾讯官方微信号“手机充值”（微信号：wxhuafei）点击底部菜单--客户服务--订单查询与投诉，进行申诉。也可登陆淘宝或支付宝，进入“我的订单--联系客服”，进行订单情况咨询及投诉。")#line:302
            if (OOOOO000O00O0000O =="balance_nocorrect"):OO0O000OO0O00OOOO .append ("话费余额查询不准确：\n您好，话费信息可能存在一定时间的延迟，如您对查询结果有疑义，建议您通过移动官网查询账单。")#line:303
            if (OOOOO000O00O0000O =="balance_search"):OO0O000OO0O00OOOO .append ("话费余额的其他查询方式：\n您可编辑“CXYE”发至10086，即可查询预存或余额。")#line:304
            if (OOOOO000O00O0000O =="rechagre_method"):OO0O000OO0O00OOOO .append ("话费、流量的充值方式：\n您可关注“中国移动10086”官方微信，点击“我要办理—充流量充话费—话费充值”，即可进行充值并享受优惠；也可以使用充值卡、银行卡、银行托收或营业厅及代收点等方式缴费。\n您可关注“中国移动10086”官方微信，点击“我要办理—充流量充话费—流量充值”，即可进行充值并享受优惠。")#line:305
            if (OOOOO000O00O0000O =="password_retrieve"):OO0O000OO0O00OOOO .append ("我的服务密码如何找回：\n全球通客户编辑短信“MMCZ空格证件号码空格新密码空格新密码”发送至10086，即可为本机重置客户服务密码。证件号码是您入网时登记的身份证、护照、军官证等有效身份证件信息。输入的密码需是6位数字，且两次输入的新密码完全相同。每月最后一天19点后不受理。\n另外，全球通、动感地带、神州行客户，还可通过门户网站重置密码。登录北京移动网站（ www.bj.10086.cn ），在右上角搜索栏中输入“客服密码业务”，根据提示操作并验证相关客户资料后即可重置密码。温馨提示：新密码请设置为6位数字，不要使用相同数字、顺序数字、倒序数字、本手机号码中的连续数字、身份证件中的连续数字等个人信息作为您的密码。")#line:306
            if (OOOOO000O00O0000O =="password_change"):OO0O000OO0O00OOOO .append ("服务密码修改")#line:307
            if (OOOOO000O00O0000O =="password_search"):OO0O000OO0O00OOOO .append ("服务密码查询")#line:308
            if (OOOOO000O00O0000O =="password_reset"):OO0O000OO0O00OOOO .append ("我的服务密码泄露需要重置：\n全球通客户编辑短信“MMCZ空格证件号码空格新密码空格新密码”发送至10086，即可为本机重置客户服务密码。证件号码是您入网时登记的身份证、护照、军官证等有效身份证件信息。输入的密码需是6位数字，且两次输入的新密码完全相同。每月最后一天19点后不受理。\n另外，全球通、动感地带、神州行客户，还可通过门户网站重置密码。登录北京移动网站（ www.bj.10086.cn ），在右上角搜索栏中输入“客服密码业务”，根据提示操作并验证相关客户资料后即可重置密码。温馨提示：新密码请设置为6位数字，不要使用相同数字、顺序数字、倒序数字、本手机号码中的连续数字、身份证件中的连续数字等个人信息作为您的密码。")#line:309
            if (OOOOO000O00O0000O =="password_intro"):OO0O000OO0O00OOOO .append ("服务密码是什么：\n客户服务密码是您在入网时获得的密码，可用于在网站、营业厅等渠道查询账详单、办理业务等。温馨提示：客服密码为6位数字，请您将客服密码设置为排列不规律的密码，请不要使用相同数字、顺序数字、倒序数字???本手机号码中的连续数字、身份证件中的连续数字等个人信息作为您的密码。")#line:310
            if (OOOOO000O00O0000O =="addedservice_close"):OO0O000OO0O00OOOO .append ("如何查询退订本机增值业务：\n“增值业务0000统一查询退订”是一项针对客户已订制业务的便捷查询退订服务。客户只要发送“0000”到10086，即可查询本机截至目前订制的包月类增值业务。查询结果包括业务提供商、业务名称和业务标准资费。值得注意的是，如果所查询到的某项业务为套餐内免费赠送，或为半年/年套餐资费优惠包，且套餐和优惠包在有效期内，“0000”查询结果所示资费仅为该业务的标准资费展示，不会再另行收取费用。实际发生费用以客户的月度话费账单为准。此外，如果客户不再需要某项业务，也可根据查询结果，回复相应业务名称前的数字序号即可退订。")#line:311
            if (OOOOO000O00O0000O =="addedservice_search"):OO0O000OO0O00OOOO .append ("如何查询退订本机增值业务：\n“增值业务0000统一查询退订”是一项针对客户已订制业务的便捷查询退订服务。客户只要发送“0000”到10086，即可查询本机截至目前订制的包月类增值业务。查询结果包括业务提供商、业务名称和业务标准资费。值得注意的是，如果所查询到的某项业务为套餐内免费赠送，或为半年/年套餐资费优惠包，且套餐和优惠包在有效期内，“0000”查询结果所示资费仅为该业务的标准资费展示，不会再另行收取费用。实际发生费用以客户的月度话费账单为准。此外，如果客户不再需要某项业务，也可根据查询结果，回复相应业务名称前的数字序号即可退订。")#line:312
            if (OOOOO000O00O0000O =="bill_search"):OO0O000OO0O00OOOO .append ("详细通话记录与消费查询：\n您可通过北京移动门户网站查询近6个月的通话记录以及消费记录情况。")#line:313
            if (OOOOO000O00O0000O =="bill_error"):OO0O000OO0O00OOOO .append ("账单显示有误怎么核实：\n您可先通过“中国移动10086”微信公众号查询月账单的情况，如仍显示有误，可再通过详单判断本月月租、通话费、上网费、短信费等内容是否正确。当确认存在问题，可将出现的具体问题进行记录，拨打10086人工进行反馈及确认。")#line:314
            if (OOOOO000O00O0000O =="bill_incomplete"):OO0O000OO0O00OOOO .append ("账单显示信息不完整：\n您可登陆“中国移动10086”微信公众号，查询月账单内容。如仍不完整，可拨打10086人工进行反馈及确认。")#line:315
if __name__ =="__main__":#line:401
    tmp =tmp_a ()#line:402

