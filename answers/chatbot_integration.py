#encoding=utf-8
import re
import sys

import jieba
import jieba.posseg as pseg


#reload(sys)
#sys.setdefaultencoding('utf8')

def and_condition(lst1):
    pass

def or_condition(lst1,lst2):
    pass

def only_condition(lst1):
    pass

def reject_condition(lst1):
    pass


class tmp_a:
    def __init__(self):
        self.zt = ["不能", "无法", "没法", "不足", "不了","不够","不多","欠费"]  # 21
        self.zt1 = ["欠费了","不够了","不足了","停机了"]

        self.noaccount_needadd1 = ["充值了","充了","充钱了","冲了","交了","充过"] #19
        self.noaccount_needadd2 = ["不能", "无法", "没法","不足","不了"] #20
        self.noaccount_keywords_1 = ["充","充值了","充了","冲","冲了","交了","充值","缴费","交费","充话费","交","充过"] #8
        self.noaccount_keywords = ["没显示","没有显示","没反应","没有反应","没有收到","没收到","没增加","没有增加","没提示","没有提示"
                                   "停机","打不出去","还不通","还欠费","没到","没有到","欠费","欠","停机","不能", "无法", "没法","没变","没钱"]
        self.noaccount_keywords_2 = ["没到账","没有到账","没给充上","没有充上","不到账","未到账","不进账"] #10

        self.nook_keyword2 = ["有","还有"]
        self.nook_keyword3 = ["钱","余额","元"]

        self.nook_keyword = ["只到了","只到账","不对","只有","只剩","只","少了","不准确","就剩","怎么剩","就还剩","应该还剩",
                             "不一致","不一样","对不上","打不出去","打不通","不能", "无法", "没法","有问题","有点问题"] #9
        self.nook_keyword1 = ["话费","余额","查话费"] #18

        self.noaccount_exceptwords = ["兑换", "流量", "积分", "宽带","星级","游戏","电子券","活动","发票","充错","会员","打印发票","送"]
        self.noaccount_keywords_3  = ["微信公众号","公众号","app","客户端","掌厅","掌上营业厅"] #17

        self.huafei_1 = ["充","交","冲","冲话费","充流量","充话费","充值","充钱","缴费"] #1
        self.huafei_2 = ["方法","哪里","怎么","方式","如何","渠道","我想","我要","想","要","咋","怎样"] #2
        self.huafei_3 = ["发票","开发票","q","qb","qq币","qq","打印发票","记录","电费","座机","固定电话","会员","扣币"] #3
        self.huafei_4 = ["刚","刚刚","积分", "宽带","星级","游戏","电子券","活动","兑换","固话","开机","漫游","语音","扣","账单","明细","详单"] #16
        self.huafei_5 = ["知道","了解"]

        self.yue_1 = ["查","查询"] #11
        self.yue_2 = ["话费","钱","余额"] #12
        self.yue_3 = ["剩","剩余","有多少","还有多少"] #13
        self.yue_4 = ["查话费","余额"]#14

        self.tkz = jieba.Tokenizer()
        from answers.word_dictionary import Dictionary
        for i in Dictionary.meword:
            elem = i.split(' ')
            if len(elem) == 1:
                self.tkz.add_word(i)
            elif len(elem) == 2:
                self.tkz.add_word(elem[0], tag=elem[1])
            else:
                self.tkz.add_word(elem[0], tag=elem[2], freq=int(elem[1]))
            # self.tkz.load_userdict("meword")
        self.psegp = pseg.POSTokenizer(self.tkz)

    def process_charge(self,line,lst):
        line = line.replace("帐","账")
        line = line.lower()

        words = self.psegp.cut(line)
        word_count = 0

        flag = False
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        flag5 = False
        flag6 = False
        flag7 = False
        flag8 = False
        flag9 = False
        flag10 = False

        flag11 = False
        flag12 = False
        flag13 = False
        flag14 = False
        flag15 = False
        flag16 = False
        flag17 = False
        flag18 = False

        flag19 = False
        flag20 = False

        flag21 = False
        flag22 = False
        flag23 = False
        flag24 = False

        flag25 = False

        subsen_lst = []
        word_lst = []
        for word, pos in words:
            #print word,pos

            word_count += 1

            if(pos == "x"):
                subsen_lst.append(word_lst)
                word_lst = []
                if not (flag1 and flag2):
                    flag1 = False
                    flag2 = False
            else:
                word_lst.append((word,pos))

            if (word in self.huafei_1): flag1 = True
            if (word in self.huafei_2): flag2 = True
            if (word in self.huafei_3): flag3 = True
            if (word in self.huafei_4): flag16 = True
            if (pos == "v" and word not in self.huafei_1 and word not in self.huafei_5):
                flag3 = True
            if (pos == "zt" or pos == "qd"):
                flag3 = True
            if(pos == "x" and ((flag1 == True and flag2 == False) or (flag1 == False and flag2 == True))):
                flag3 = True

            if (word in self.yue_1): flag11 = True
            if (word in self.yue_2): flag12 = True
            if (word in self.yue_3): flag13 = True
            if (word in self.yue_4): flag14 = True
            if (pos == "zq"): flag15 = True

            if (word in self.noaccount_keywords_2): flag10 = True
            if (word in self.nook_keyword): flag9 = True
            if (word in self.nook_keyword1): flag18 = True
            if (word in self.noaccount_keywords_1): flag8 = True
            if (word in self.noaccount_keywords): flag4 = True
            if (word in self.noaccount_exceptwords): flag5 = True
            if (word == "10086"): flag6 = True
            if (word in self.noaccount_keywords_3): flag17 = True
            if (word in ["微信", "支付宝"]): flag7 = True

            if (word in self.noaccount_needadd1): flag19 = True
            if (word in self.noaccount_needadd2): flag20 = True

            if (word in self.zt): flag21 = True
            if (flag1 and flag2 and flag21 == False): flag22 = True
            if (flag1  == False and flag2  == False and flag21): flag23 = True
            if (flag1 and flag2 and flag23): flag24 = True

            if (word in self.zt1): flag25 = True

        if len(word_lst) > 0: subsen_lst.append(word_lst)

        #print flag5, flag25
        if(flag5 == False and flag25 == False):
            if (flag10 or (flag4 and flag8) or (flag19 and flag20)):
                if (flag6 and flag17): lst.append("noaccount_10086")
                elif(flag7): lst.append("noaccount_weixin")
                else: lst.append("noaccount")
                flag = True

        #print flag9,flag8,flag18,flag5,flag22,flag24
        if (flag9 and (flag8 or flag18) and flag5 == False and flag22 == False and flag24 == False):
            lst.append("balance_nocorrect")
            flag = True

        #print flag1, flag2, flag3, flag16,flag19
        if (flag == False and flag19 == False and flag10 == False and flag3 == False and flag16 == False and flag1 and flag2):
            lst.append("rechagre_method")
            flag = True

        if (flag1 and word_count == 1):
            lst.append("rechagre_method")
            flag = True

        if (flag == False and flag19 == False and flag10 == False):
            for subsen in subsen_lst:
                flag1 = False
                flag2 = False
                flag3 = False
                flag16 = False
                for word,pos in subsen:
                    if (word in self.huafei_1): flag1 = True
                    if (word in self.huafei_2): flag2 = True
                    if (word in self.huafei_3): flag3 = True
                    if (word in self.huafei_4): flag16 = True
                    if (pos == "v" and word not in self.huafei_1 and word not in self.huafei_5): flag3 = True
                #print flag1,flag2,flag3,flag16
                if (flag3 == False and flag16 == False and flag1 and flag2):
                    lst.append("rechagre_method")
                    flag = True
                    break

        #print flag11, flag13, flag12
        if (flag == False and flag15 == False and flag5 == False and flag16 == False):
            if (((flag11 or flag13) and flag12) or (flag2 and flag14)):
                lst.append("balance_search")
                flag = True

            if (flag14 and word_count == 1):
                lst.append("balance_search")
                flag = True

        #if(flag == False): print "无法理解"

    def process_password(self,line,lst):
        if (line.find("密码") >= 0 or line.find("蜜码") >= 0):
            if(line.find("服务") >= 0 or line.find("客服") >= 0):
                if (line.find("忘") >= 0 or line.find("记") >= 0 or line.find("找回") >= 0 or line.find("不知道") >= 0
                    or line.find("找到") >= 0 or line.find("不对") >= 0):
                    lst.append("password_retrieve")
                elif (line.find("改") >= 0 or line.find("更换") >= 0 or line.find("重置") >= 0 or line.find("重设") >= 0  or line.find("重新设") >= 0
                      or line.find("盗") >= 0 or line.find("泄露") >= 0):
                    lst.append("password_reset")
                elif ((line.find("是什么") >= 0 or line.find("什么是") >= 0 or line.find("介绍") >= 0
                       or line.find("啥叫") >= 0 or line.find("是啥") >= 0 or line.find("意思") >= 0
                       or line.find("用来") >= 0 or line.find("获取") >=0)
                      and line.find("不") < 0 and line.find("锁") < 0):
                    lst.append("password_intro")
                elif (line.find("查") >= 0 or line.find("多少") >= 0):
                    lst.append("password_search")

    def process_addedservice(self,line,lst):
        if (line.find("增值业务") >= 0 or line.find("增值服务") >= 0):
            if (line.find("影响") < 0 and line.find("为什么") < 0):
                if ((line.find("取消") >= 0 or line.find("关") >= 0 or line.find("退") >= 0 or line.find("停") >= 0
                     or line.find("删") >= 0
                     or line.find("撤") >= 0 or line.find("解除") >= 0 or line.find("消除") >= 0 or line.find("去除") >= 0)
                    and ((line.find("不") < 0 and line.find("有没有") < 0) or line.find("可不可以") >= 0
                         or line.find("不要") >= 0 or line.find("不需要") >= 0 or line.find("不想") >=0 )):
                    lst.append("addedservice_close")
                elif (line.find("查") >= 0 or line.find("看") >= 0 or line.find("哪些") >= 0 or line.find("有什么") >= 0
                      or line.find("什么增值业务") >= 0 or line.find("有没有") >= 0):
                    lst.append("addedservice_search")

    def process_bill(self,line,lst):
        pattern = re.compile("(账单|帐单|明细|话单|详单|详情|((通话|通讯|电话|话费|消费)(记录|纪录)))$")

        if (line.find("账单") >= 0 or line.find("记录") >= 0 or line.find("帐单") >= 0 or line.find("纪录") >= 0 or line.find("明细") >= 0
            or line.find("详单") >= 0 or line.find("话单") >= 0):
            search_flag = False
            error_flag = False
            incomplete_flag = False

            if (line.find("发票") < 0 and line.find("打印") < 0 and line.find("下载") < 0 and line.find("139邮箱") < 0
                and line.find("密码") < 0 and line.find("139信箱") < 0):
                m = pattern.search(line)
                if ((line.find("查") >= 0 or line.find("看") >= 0 or line.find("获取") >= 0)
                     and (((line.find("通话") >= 0 or line.find("话费") >= 0 or line.find("通信") >= 0 or line.find("消费") >= 0
                          or line.find("费用") >= 0 or line.find("电话") >= 0)
                          and (line.find("记录") >= 0 or line.find("纪录") >= 0 or line.find("明细") >= 0)) or
                    (line.find("账单") >= 0 or line.find("帐单") >= 0 or line.find("详单") >= 0 or line.find("话单") >= 0))
                    and (line.find("为什么") < 0 and line.find("充值") < 0)):
                    lst.append("bill_search")
                    search_flag = True
                elif (m):
                    lst.append("bill_search")
                    search_flag = True

                if(search_flag == False):
                    if ((((line.find("通话") >= 0 or line.find("话费") >= 0 or line.find("通信") >= 0 or line.find("消费") >= 0
                              or line.find("费用") >= 0)
                              and (line.find("明细") >= 0)) or
                        (line.find("账单") >= 0 or line.find("帐单") >= 0 or line.find("详单") >= 0 ))
                        and (line.find("有误") >= 0 or line.find("有问题") >= 0 or line.find("有错") >= 0 or line.find("多了") >= 0
                             or line.find("多出") >= 0 or line.find("多扣") >= 0 or line.find("不对") >= 0 or line.find("错误") >= 0
                             or line.find("错了") >= 0 or line.find("不正确") >= 0 or line.find("不准确") >= 0 or line.find("有点问题") >= 0
                             or line.find("异常") >= 0 or line.find("少了") >= 0 or line.find("这么多") >= 0)):
                        lst.append("bill_error")
                        error_flag = True

                    if(error_flag == False):
                        if (line.find("没显示") >=0 or line.find("没有显示") >=0 or line.find("不完整") >= 0 or line.find("一部分") >= 0 or
                                line.find("不全") >= 0 or line.find("没有记录") >= 0 or line.find("没记录") >= 0):
                            lst.append("bill_incomplete")

    def predict(self,line,replylst):
        # reload(sys)
        # sys.setdefaultencoding('utf8')

        lst = []
        self.process_charge(line, lst)
        self.process_password(line, lst)
        self.process_addedservice(line, lst)
        self.process_bill(line, lst)

        for res in lst:
            if (res == "noaccount_10086"): replylst.append("10086客户端、10086微信公众号充值未到账:\n您好，若出现您的支付账户已经扣款成功，但手机账户未查询到充值记录的情况，可能是由于银联方或其他支付方转账耗时产生延误，或某时段充值用户较多，系统繁忙等原因。建议您耐心等待，您也可以核对一下充值号码是否准确。")
            if (res == "noaccount_weixin"): replylst.append("微信支付、支付宝充值未到账：\n您可以通过发送短信“CXYE”到10086，查询自己的话费是否有增加，如增加，且与充值的金额一致，那则表示充值正常。若话费没有增加，可使用腾讯官方微信号“手机充值”（微信号：wxhuafei）点击底部菜单--客户服务--订单查询与投诉，进行申诉。也可登陆淘宝或支付宝，进入“我的订单--联系客服”，进行订单情况咨询及投诉。")
            if (res == "noaccount"):
                replylst.append("10086客户端、10086微信公众号充值未到账:\n您好，若出现您的支付账户已经扣款成功，但手机账户未查询到充值记录的情况，可能是由于银联方或其他支付方转账耗时产生延误，或某时段充值用户较多，系统繁忙等原因。建议您耐心等待，您也可以核对一下充值号码是否准确。\n"
                                "微信支付、支付宝充值未到账：\n您可以通过发送短信“CXYE”到10086，查询自己的话费是否有增加，如增加，且与充值的金额一致，那则表示充值正常。若话费没有增加，可使用腾讯官方微信号“手机充值”（微信号：wxhuafei）点击底部菜单--客户服务--订单查询与投诉，进行申诉。也可登陆淘宝或支付宝，进入“我的订单--联系客服”，进行订单情况咨询及投诉。")
            if (res == "balance_nocorrect"): replylst.append("话费余额查询不准确：\n您好，话费信息可能存在一定时间的延迟，如您对查询结果有疑义，建议您通过移动官网查询账单。")
            if (res == "balance_search"): replylst.append("话费余额的其他查询方式：\n您可编辑“CXYE”发至10086，即可查询预存或余额。")
            if (res == "rechagre_method"): replylst.append("话费、流量的充值方式：\n您可关注“中国移动10086”官方微信，点击“我要办理—充流量充话费—话费充值”，即可进行充值并享受优惠；也可以使用充值卡、银行卡、银行托收或营业厅及代收点等方式缴费。\n您可关注“中国移动10086”官方微信，点击“我要办理—充流量充话费—流量充值”，即可进行充值并享受优惠。")
            if (res == "password_retrieve"): replylst.append("我的服务密码如何找回：\n全球通客户编辑短信“MMCZ空格证件号码空格新密码空格新密码”发送至10086，即可为本机重置客户服务密码。证件号码是您入网时登记的身份证、护照、军官证等有效身份证件信息。输入的密码需是6位数字，且两次输入的新密码完全相同。每月最后一天19点后不受理。\n另外，全球通、动感地带、神州行客户，还可通过门户网站重置密码。登录北京移动网站（ www.bj.10086.cn ），在右上角搜索栏中输入“客服密码业务”，根据提示操作并验证相关客户资料后即可重置密码。温馨提示：新密码请设置为6位数字，不要使用相同数字、顺序数字、倒序数字、本手机号码中的连续数字、身份证件中的连续数字等个人信息作为您的密码。")
            if (res == "password_change"): replylst.append("服务密码修改")
            if (res == "password_search"): replylst.append("服务密码查询")
            if (res == "password_reset"): replylst.append("我的服务密码泄露需要重置：\n全球通客户编辑短信“MMCZ空格证件号码空格新密码空格新密码”发送至10086，即可为本机重置客户服务密码。证件号码是您入网时登记的身份证、护照、军官证等有效身份证件信息。输入的密码需是6位数字，且两次输入的新密码完全相同。每月最后一天19点后不受理。\n另外，全球通、动感地带、神州行客户，还可通过门户网站重置密码。登录北京移动网站（ www.bj.10086.cn ），在右上角搜索栏中输入“客服密码业务”，根据提示操作并验证相关客户资料后即可重置密码。温馨提示：新密码请设置为6位数字，不要使用相同数字、顺序数字、倒序数字、本手机号码中的连续数字、身份证件中的连续数字等个人信息作为您的密码。")
            if (res == "password_intro"): replylst.append("服务密码是什么：\n客户服务密码是您在入网时获得的密码，可用于在网站、营业厅等渠道查询账详单、办理业务等。温馨提示：客服密码为6位数字，请您将客服密码设置为排列不规律的密码，请不要使用相同数字、顺序数字、倒序数字???本手机号码中的连续数字、身份证件中的连续数字等个人信息作为您的密码。")
            if (res == "addedservice_close"): replylst.append("如何查询退订本机增值业务：\n“增值业务0000统一查询退订”是一项针对客户已订制业务的便捷查询退订服务。客户只要发送“0000”到10086，即可查询本机截至目前订制的包月类增值业务。查询结果包括业务提供商、业务名称和业务标准资费。值得注意的是，如果所查询到的某项业务为套餐内免费赠送，或为半年/年套餐资费优惠包，且套餐和优惠包在有效期内，“0000”查询结果所示资费仅为该业务的标准资费展示，不会再另行收取费用。实际发生费用以客户的月度话费账单为准。此外，如果客户不再需要某项业务，也可根据查询结果，回复相应业务名称前的数字序号即可退订。")
            if (res == "addedservice_search"): replylst.append("如何查询退订本机增值业务：\n“增值业务0000统一查询退订”是一项针对客户已订制业务的便捷查询退订服务。客户只要发送“0000”到10086，即可查询本机截至目前订制的包月类增值业务。查询结果包括业务提供商、业务名称和业务标准资费。值得注意的是，如果所查询到的某项业务为套餐内免费赠送，或为半年/年套餐资费优惠包，且套餐和优惠包在有效期内，“0000”查询结果所示资费仅为该业务的标准资费展示，不会再另行收取费用。实际发生费用以客户的月度话费账单为准。此外，如果客户不再需要某项业务，也可根据查询结果，回复相应业务名称前的数字序号即可退订。")
            if (res == "bill_search"): replylst.append("详细通话记录与消费查询：\n您可通过北京移动门户网站查询近6个月的通话记录以及消费记录情况。")
            if (res == "bill_error"): replylst.append("账单显示有误怎么核实：\n您可先通过“中国移动10086”微信公众号查询月账单的情况，如仍显示有误，可再通过详单判断本月月租、通话费、上网费、短信费等内容是否正确。当确认存在问题，可将出现的具体问题进行记录，拨打10086人工进行反馈及确认。")
            if (res == "bill_incomplete"): replylst.append("账单显示信息不完整：\n您可登陆“中国移动10086”微信公众号，查询月账单内容。如仍不完整，可拨打10086人工进行反馈及确认。")

    # def test(self):
    #     reload(sys)
    #     sys.setdefaultencoding('utf8')
    #
    #
    #     print "开始测试.....（输入\"exit\"退出）"
    #     while(1):
    #         line = raw_input("用户问题：")
    #         if (line == "exit"):
    #             break
    #
    #         lst = []
    #         self.process_charge(line,lst)
    #         self.process_password(line,lst)
    #         self.process_addedservice(line,lst)
    #         self.process_bill(line,lst)
    #
    #         print "10086：",
    #         if len(lst) == 0: print "无法理解"
    #         for res in lst:
    #             if (res == "noaccount_10086"): print "10086充值未到账"
    #             if (res == "noaccount_weixin"): print "微信、支付宝充值未到账"
    #             if (res == "noaccount"): print "充值未到账"
    #             if (res == "balance_nocorrect"): print "话费余额查询不准确"
    #             if (res == "balance_search"): print "话费余额查询"
    #             if (res == "rechagre_method"): print "话费充值方法"
    #             if (res == "password_retrieve"): print "我的服务密码如何找回"
    #             if (res == "password_change"): print "服务密码修改"
    #             if (res == "password_search"): print "服务密码查询"
    #             if (res == "password_reset"): print "服务密码重置"
    #             if (res == "password_intro"): print "服务密码介绍"
    #             if (res == "addedservice_close"): print "增值业务关闭"
    #             if (res == "addedservice_search"): print "增值业务查询"
    #             if (res == "bill_search"): print "账单查询"
    #             if (res == "bill_error"): print "账单错误"
    #             if (res == "bill_incomplete"): print "账单不完整"
    #
    # def writefile(self):
    #     reload(sys)
    #     sys.setdefaultencoding('utf8')
    #
    #     Qtype_dict = {"noaccount": [], "noaccount_weixin": [], "noaccount_10086": [],
    #                    "balance_nocorrect": [],"balance_search": [], "rechagre_method": [],
    #                    "password_retrieve": [], "password_intro": [], "password_search": [],
    #                    "password_reset": [], "addedservice_search": [], "addedservice_close": [],
    #                    "bill_search": [], "bill_incomplete": [], "bill_error": []}
    #
    #     usermessage_savepath = "/home/liudt/clu/classified_corpus/total"
    #     #usermessage_savepath = "/home/liudt/pycode/output/rechagre_method"
    #     fp1 = open(usermessage_savepath, 'rb')
    #     n = 1
    #     for line in fp1:
    #         lst = []
    #         self.process_charge(line, lst)
    #         self.process_password(line, lst)
    #         self.process_addedservice(line, lst)
    #         self.process_bill(line, lst)
    #
    #         for res in lst:
    #             Qtype_dict[res].append(line)
    #         n += 1
    #         if n % 1000 == 0: print n
    #     fp1.close()
    #
    #     path = "/home/liudt/pycode/output/"
    #     filenames = Qtype_dict.keys()
    #     for filename in filenames:
    #         filepath = path+filename
    #         fp2 = open(filepath, 'wb')
    #         for line in Qtype_dict[filename]:
    #             fp2.write(line)
    #         fp2.close()
    #
    # def test1(self):
    #     #logger = logging.getLogger()
    #     #logger.setLevel(logging.NOTSET)
    #
    #     #tmp.test()
    #     replylst = []
    #     line = raw_input("请输入问题：")
    #     tmp.predict(line,replylst)
    #     for line in replylst:
    #         print line

if __name__ == "__main__":
    tmp = tmp_a()
    k=[]
    tmp.predict('我还剩多少话费',k)
    print(k)
    #tmp.test1()

    # tmp.writefile()
