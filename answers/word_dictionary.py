#coding=utf-8
class Dictionary:
    action=[
      u'安装',
      u'办理',
      u'绑定',
      u'保修',
      u'报修',
      u'拨打',
      u'补办',
      u'操作',
      u'查询',
      u'撤回',
      u'抽取',
      u'出错',
      u'催促',
      u'答复',
      u'打电话',
      u'代付',
      u'到期',
      u'到账',
      u'登录',
      u'抵消',
      u'掉线',
      u'叠加',
      u'订购',
      u'断网',
      u'兑换',
      u'返还',
      u'分享',
      u'覆盖',
      u'告诉',
      u'更改',
      u'共享',
      u'关闭',
      u'互打',
      u'互赠',
      u'恢复',
      u'回复',
      u'获赠',
      u'计算',
      u'加入',
      u'减少',
      u'缴费',
      u'接打',
      u'接听',
      u'解除',
      u'理解',
      u'连接',
      u'满足',
      u'取消',
      u'删除',
      u'上网',
      u'设置',
      u'申请',
      u'申诉',
      u'审核',
      u'升级',
      u'剩余',
      u'失败',
      u'使用',
      u'收费',
      u'搜索',
      u'提出',
      u'提前',
      u'提取',
      u'提速',
      u'替换',
      u'添加',
      u'停机',
      u'投诉',
      u'推荐',
      u'退订',
      u'忘记',
      u'维护',
      u'维修',
      u'下降',
      u'下载',
      u'显示',
      u'消费',
      u'销户',
      u'销售',
      u'携带',
      u'需要',
      u'续费',
      u'续约',
      u'寻找',
      u'邀请',
      u'预约',
      u'赠送',
      u'支付',
      u'转化',
      u'转移',
      u'转账',
      u'咨询',
      u'组成',
      ]
    askword=[
      u'何时',
      u'哪里',
      u'什么',
      u'是否',
      u'为何',
      u'怎么',
      ]
    keywords=[
      u'4G',
      u'MO生活会员',
      u'PUK',
      u'V网通',
      u'WLAN',
      u'爱分享',
      u'安心包',
      u'安心流量包',
      u'安心锁',
      u'包时套餐',
      u'备卡',
      u'被叫',
      u'本月生效',
      u'必选套餐',
      u'毕业生卡',
      u'补卡',
      u'财富通',
      u'彩铃',
      u'彩铃天地',
      u'长短号',
      u'长号',
      u'长市合一',
      u'长市话',
      u'畅游包',
      u'车卫士',
      u'充值卡',
      u'大王卡',
      u'大胃王',
      u'单宽带',
      u'单模流量',
      u'电子发票',
      u'叠加包',
      u'动感M值',
      u'动感地带',
      u'动感任我行',
      u'动感易',
      u'短号',
      u'短信',
      u'短信包',
      u'短信呼',
      u'多人组合',
      u'飞享套餐',
      u'飞信',
      u'非常假期',
      u'疯狂抓小鸡',
      u'副号',
      u'购4G手机送6G流量',
      u'关机秘书',
      u'光宽带',
      u'国际漫游',
      u'好友圈',
      u'和彩云',
      u'和动漫',
      u'和多号',
      u'和积分',
      u'和家庭',
      u'和教育',
      u'和宽带',
      u'和视界',
      u'和微币',
      u'和校园',
      u'和游戏',
      u'和娱乐',
      u'呼出限制',
      u'话费',
      u'积分',
      u'集团V',
      u'集团V套餐',
      u'集团V网',
      u'集团V网组',
      u'集团V业务',
      u'集团彩铃',
      u'集团号',
      u'集团网',
      u'集团业务',
      u'家庭V网',
      u'家庭号',
      u'家庭号码',
      u'家庭宽带',
      u'家庭网',
      u'家庭业务',
      u'家园卡',
      u'假日流量',
      u'教育优学',
      u'教育优学套餐',
      u'可选包',
      u'快餐包',
      u'快捷方式',
      u'宽带',
      u'宽带E',
      u'宽带网',
      u'来电提醒',
      u'来电显示',
      u'立即生效',
      u'连号',
      u'两城一号',
      u'两城一家',
      u'铃音盒',
      u'零首充',
      u'流量包',
      u'流量大胃王',
      u'流量红包',
      u'流量王',
      u'流量至尊包',
      u'裸宽带',
      u'买一送一',
      u'漫游费',
      u'每日一笑',
      u'咪咕',
      u'咪咕会员',
      u'农机通',
      u'农信通',
      u'品牌套餐',
      u'气象通',
      u'抢流量',
      u'亲情号',
      u'亲情号码',
      u'亲情网',
      u'亲情业务',
      u'轻松卡',
      u'轻松聊',
      u'情侣包',
      u'全国流量',
      u'全球通',
      u'让红包飞',
      u'人工服务',
      u'任我行',
      u'任意玩',
      u'三元包',
      u'商城币',
      u'商旅套餐',
      u'神州行',
      u'生活百科',
      u'生日套餐',
      u'省内V网',
      u'省内流量',
      u'实名认证',
      u'实名制',
      u'手机电视',
      u'手机宽带',
      u'随E行',
      u'随意宝',
      u'随意玩',
      u'套餐易',
      u'特享包',
      u'停机保号',
      u'通用流量',
      u'同事网',
      u'网内长市话',
      u'五元包',
      u'乡村套餐',
      u'乡村网',
      u'乡亲网',
      u'乡情网',
      u'校信通',
      u'校讯通',
      u'校园E套餐',
      u'校园宽带',
      u'校园行',
      u'新春换旧',
      u'信号',
      u'信用金',
      u'行车小秘书',
      u'幸运开机',
      u'学而优',
      u'夜话无眠',
      u'夜间流量',
      u'夜猫包',
      u'一带一路',
      u'一卡多号',
      u'一卡双号',
      u'一年',
      u'一元包',
      u'移动400',
      u'移动宽带',
      u'移动梦网',
      u'以旧换新',
      u'易查询',
      u'易充值',
      u'易缴费',
      u'优惠包',
      u'优教育',
      u'有线宽带',
      u'月结日',
      u'月套餐',
      u'月消费',
      u'月账单',
      u'阅读费',
      u'悦读会',
      u'云宽带',
      u'砸金蛋',
      u'増值业务',
      u'增值费',
      u'增值服务',
      u'政企一卡通',
      u'政务通',
      u'政务一卡通',
      u'至尊包',
      u'中国文化学堂',
      u'主号',
      u'主卡',
      u'主套餐',
      u'抓小鸡',
      u'专用流量',
      u'捉小鸡',
      u'自选套餐',
      u'自选语音包',
      u'自由增值费',
      u'自有增值费',
      u'自有增值业务',
      ]
    meword=[
      u'10086 1000 qd',
      u'1008611 1000 qd',
      u'app 1000 qd',
      u'不到账 5 zt',
      u'不对 5000 zt',
      u'不进账 5 zt',
      u'不准确 50 xrc',
      u'充话费 5 dz',
      u'充了 50 dz',
      u'充流量 5 dz',
      u'充值卡 1000 qd',
      u'打不出去 5 zt',
      u'到账 5 zt',
      u'电子券 1000 qd',
      u'公众号 1000 qd',
      u'固定电话 1000 zm',
      u'官网 1000 qd',
      u'还不通 5 zt',
      u'还欠费 5 zt',
      u'还有多少 500 yw',
      u'和积分 500 n',
      u'积分 50000 n',
      u'交了 500 dz',
      u'缴费 5 dz',
      u'就还剩 5 zt',
      u'就剩 50 zt',
      u'客户端 1000 qd',
      u'空中充值 1000 qd',
      u'没到账 5 zt',
      u'没反应 50 zt',
      u'没给充上 5 zt',
      u'没收到 5 zt',
      u'没显示 50 zt',
      u'没有充上 5 zt',
      u'没有到 500 zt',
      u'没有到账 5 zt',
      u'没有增加 50 zt',
      u'少了 500 zt',
      u'微信 1000 qd',
      u'微信公众号 1000 qd',
      u'未到账 5 zt',
      u'我想 500 yt',
      u'我要 500 yt',
      u'一个月 500 zq',
      u'应该还剩 5 zt',
      u'有多少 500 yw',
      u'怎么剩 5 zt',
      u'支付宝 1000 qd',
      u'只到了 50 zt',
      u'只到账 5 zt',
      u'只剩 5 zt',
      u'只有 5000 zt',
      u'自助交费机 1000 qd',
      ]
    newaction=[
      u'绑定',
      u'包含',
      u'包括',
      u'保持',
      u'保存',
      u'保留',
      u'报销',
      u'逼',
      u'变',
      u'拨打',
      u'拨号',
      u'不变',
      u'不得',
      u'不懂',
      u'不符',
      u'不够',
      u'不见',
      u'不能用',
      u'补',
      u'补偿',
      u'补交',
      u'参与',
      u'操作',
      u'测试',
      u'查不到',
      u'查出来',
      u'查询',
      u'超出',
      u'超过',
      u'撤回',
      u'成为',
      u'承诺',
      u'冲突',
      u'抽取',
      u'出差',
      u'出国',
      u'出去',
      u'出现',
      u'处于',
      u'促销',
      u'存在',
      u'错误',
      u'达到',
      u'答复',
      u'打不开',
      u'打开',
      u'打扰',
      u'打算',
      u'打印',
      u'代办',
      u'代替',
      u'到账',
      u'登记',
      u'登录',
      u'等待',
      u'抵达',
      u'抵扣',
      u'抵消',
      u'点播',
      u'点击',
      u'调',
      u'调整',
      u'掉线',
      u'叠加',
      u'订购',
      u'订过',
      u'订阅',
      u'定制',
      u'丢失',
      u'动',
      u'冻结',
      u'断网',
      u'兑奖',
      u'兑现',
      u'发不出',
      u'发出',
      u'发到',
      u'发放',
      u'发给',
      u'发送',
      u'发现',
      u'发信息',
      u'反馈',
      u'反应',
      u'返还',
      u'返回',
      u'访问',
      u'分摊',
      u'分享',
      u'服务',
      u'符合',
      u'负责',
      u'复制',
      u'改变',
      u'改不了',
      u'搞',
      u'更改',
      u'工作',
      u'共享',
      u'沟通',
      u'购买',
      u'挂',
      u'挂失',
      u'关闭',
      u'关注',
      u'观看',
      u'管',
      u'管理',
      u'过户',
      u'呼叫',
      u'花',
      u'划算',
      u'换成',
      u'换回',
      u'换机',
      u'回答',
      u'回复',
      u'回来',
      u'回去',
      u'活动',
      u'获取',
      u'计费',
      u'计算',
      u'记得',
      u'寄',
      u'加不进',
      u'加价',
      u'加上',
      u'加油',
      u'加载',
      u'检查',
      u'减免',
      u'减少',
      u'降低',
      u'交错',
      u'缴费',
      u'接不到',
      u'接到',
      u'接受',
      u'接听',
      u'接通',
      u'结束',
      u'截图',
      u'截止',
      u'解绑',
      u'解答',
      u'解冻',
      u'解决',
      u'解释',
      u'介绍',
      u'仅限',
      u'进',
      u'进不去',
      u'进来',
      u'进去',
      u'禁止',
      u'举报',
      u'开具',
      u'开始',
      u'看不出',
      u'看不到',
      u'考虑',
      u'可用',
      u'扣费',
      u'扣款',
      u'快递',
      u'拦截',
      u'了解',
      u'类似',
      u'累积',
      u'理解',
      u'连不上网',
      u'连接',
      u'领取',
      u'留言',
      u'满意',
      u'漫游',
      u'忙',
      u'没法',
      u'没收到',
      u'没有',
      u'免',
      u'免流',
      u'拿',
      u'拿到',
      u'判断',
      u'评',
      u'欺骗',
      u'签',
      u'签到',
      u'欠',
      u'欠费',
      u'强行',
      u'抢',
      u'切换',
      u'清零',
      u'请求',
      u'求',
      u'取',
      u'取掉',
      u'取消',
      u'确定',
      u'认证',
      u'融合',
      u'入网',
      u'骚扰',
      u'删除',
      u'闪',
      u'上报',
      u'上传',
      u'上网',
      u'设置',
      u'申诉',
      u'审核',
      u'升级',
      u'剩余',
      u'失败',
      u'失望',
      u'识别',
      u'使用',
      u'试用',
      u'收不到',
      u'收到',
      u'收取',
      u'受理',
      u'售卖',
      u'输',
      u'输入',
      u'属于',
      u'刷新',
      u'睡觉',
      u'说法',
      u'说好',
      u'说话',
      u'死',
      u'送到',
      u'送花',
      u'搜索',
      u'锁定',
      u'提',
      u'提高',
      u'提供',
      u'提交',
      u'提前',
      u'提示',
      u'提速',
      u'添加',
      u'填写',
      u'听',
      u'通用',
      u'通知',
      u'透支',
      u'推',
      u'推荐',
      u'推送',
      u'退出',
      u'退还',
      u'退回',
      u'完',
      u'完成',
      u'忘记',
      u'违规',
      u'维护',
      u'未到账',
      u'未知',
      u'无限',
      u'喜欢',
      u'下班',
      u'下降',
      u'下月生效',
      u'下载',
      u'显',
      u'显示',
      u'限速',
      u'限制',
      u'享受',
      u'消除',
      u'消费',
      u'销户',
      u'携带',
      u'写',
      u'信任',
      u'修理',
      u'虚拟',
      u'需要',
      u'续约',
      u'选择',
      u'寻找',
      u'延时',
      u'验证',
      u'邀请',
      u'摇',
      u'要求',
      u'应用',
      u'营销',
      u'赢',
      u'影响',
      u'用不完',
      u'用到',
      u'用于',
      u'优惠',
      u'优先',
      u'邮寄',
      u'有没有',
      u'有误',
      u'有用',
      u'预存',
      u'预付',
      u'预计',
      u'预约',
      u'遇到',
      u'原有',
      u'允许',
      u'造成',
      u'增加',
      u'增值',
      u'赠送',
      u'诈骗',
      u'找到',
      u'找回',
      u'整',
      u'支持',
      u'支付',
      u'指定',
      u'重启',
      u'主叫',
      u'注册',
      u'注意',
      u'转接',
      u'转送',
      u'转网',
      u'转为',
      u'转移',
      u'转赠',
      u'准备',
      u'咨询',
      u'自选',
      u'自助',
      u'总计',
      u'走',
      u'租',
      ]
    newstop=[
      u'$',
      u'阿',
      u'啊',
      u'哎呀',
      u'昂',
      u'把',
      u'吧',
      u'帮',
      u'帮我',
      u'抱歉',
      u'被',
      u'呗',
      u'本来',
      u'比较',
      u'不好意思',
      u'不是',
      u'不知道',
      u'才能',
      u'查下',
      u'大概',
      u'大约',
      u'到底',
      u'的',
      u'的话',
      u'的么',
      u'都',
      u'刚',
      u'刚才',
      u'刚刚',
      u'个',
      u'给我',
      u'根本',
      u'关于',
      u'hello',
      u'哈',
      u'哈咯',
      u'哈哈哈',
      u'哈喽',
      u'好像',
      u'呵呵',
      u'和',
      u'嗨喽',
      u'很',
      u'哗哗哗',
      u'几乎',
      u'家',
      u'家里',
      u'今天',
      u'进行',
      u'看见',
      u'看看',
      u'可不可以',
      u'可是',
      u'老是',
      u'了',
      u'里面',
      u'麻烦',
      u'们',
      u'明明',
      u'目前',
      u'那个',
      u'那些',
      u'那种',
      u'呢',
      u'内',
      u'能查',
      u'你好',
      u'你们',
      u'捏',
      u'您',
      u'您好',
      u'其实',
      u'亲',
      u'亲亲',
      u'请',
      u'请问',
      u'如果',
      u'时候',
      u'算了',
      u'他妈的',
      u'特么的',
      u'挺',
      u'统一',
      u'问问',
      u'问下',
      u'我办',
      u'我家',
      u'我想',
      u'卧槽',
      u'无故',
      u'无缘无故',
      u'希望',
      u'下',
      u'下来',
      u'先',
      u'现在',
      u'小姐',
      u'协助',
      u'谢谢',
      u'压根',
      u'呀',
      u'延迟',
      u'一般',
      u'一点',
      u'一份',
      u'一个',
      u'一个个',
      u'一共',
      u'一会',
      u'一会儿',
      u'一下',
      u'一下下',
      u'一下子',
      u'一些',
      u'一直',
      u'以及',
      u'以外',
      u'以为',
      u'应该',
      u'有点',
      u'有个',
      u'元',
      u'元包',
      u'原本',
      u'晕',
      u'再',
      u'在吗',
      u'怎么回事',
      u'张卡',
      u'这',
      u'这边',
      u'这个',
      u'这里',
      u'正好',
      u'之后',
      u'之间',
      u'之类',
      u'之前',
      u'知道',
      u'只是',
      u'至今',
      u'中',
      u'中有',
      u'自己',
      u'总是',
      u'最近',
      ]
    similar=[
      u'CMCC CMCCEDU CMCCWEB',
      u'E币 易币',
      u'M值 M币 动感M值',
      u'PIN PIK PUK PLN PIN码 PIK码 PUK码 PLN码 PIM PIM码',
      u'QQ 扣扣',
      u'SIM卡 手机卡 卡',
      u'USIM USIM卡 USLM',
      u'WLAN WIFE WLAM WALN WLAL WLIN WLLAN WLNA WLND WNAL WIAN WIALN WHAN WILE WIFY WIFI WI-FI 无线 无线网 无线网络',
      u'安排 安置',
      u'按钮 键',
      u'昂贵 贵',
      u'拔掉 拔出 拔除',
      u'办理 办 开通 通 刚装 开 加入 加 整 开下 安装 申报 装 安 能装 启 开启 开开 架 办个 建个 牵 要办 要包 要开 想开 想升 定下 接 拉 申请 申请加入',
      u'帮忙 帮助 帮别人 帮人 替别人 替人',
      u'帮我 帮帮我 帮助我',
      u'绑定 绑到 捆绑 绑',
      u'包含 含',
      u'保留 保有 留',
      u'备用 备份 备选',
      u'本号 本卡',
      u'本号码 此号码',
      u'本月 这个月 这月',
      u'边缘 边界',
      u'变化 变动',
      u'便携 便携式',
      u'拨打 拨',
      u'不必 不必要',
      u'不到 低于 少于',
      u'不懂 看不懂',
      u'不好 差 很差 非常差 差劲 不稳定 不太好 感觉不好',
      u'不理 不回 不回话',
      u'不能 无法 不了 不可以 不行 不可 不掉 行不通 不成',
      u'不能用 无法使用 没法用 用不了 不能使用 坏了',
      u'不愿 不想',
      u'不知 不知道',
      u'不足 缺点',
      u'补交 补发',
      u'彩铃 彩玲 彩铃网 彩领 彩铃库 炫铃',
      u'参考 参照',
      u'参与 参加',
      u'蹭取 蹭',
      u'查询 查 查查 查看 查下 查找 查一下 查一查',
      u'长号 全号',
      u'长话 长途',
      u'超出 超限 超额 超标 超量 超支 超了 超',
      u'撤回 撤出 撤销 撤消',
      u'充值券 冲值券',
      u'抽取 抽 抽到 抽奖 抽出',
      u'出错 出现异常',
      u'除去 除了 除开 除外 降下来',
      u'传输 传 传给',
      u'从没 从来不',
      u'促销 特价',
      u'催促 催',
      u'存量 余量',
      u'错误 不正确 不对 错 不准 不准确',
      u'搭配 搭',
      u'答复 回答 应答',
      u'打不通 打不进 没人接',
      u'打电话 通电话',
      u'打印 打出',
      u'大小 多大 带宽',
      u'代付 带冲 带充 代付费 代垫 代收 代收费 代冲',
      u'贷款 信用贷款',
      u'弹出 跳出',
      u'倒是 反倒是',
      u'到账 到帐 进账 上账',
      u'登记 登计',
      u'登录 登 登入 登陆',
      u'等待 等 待 等等 等会 等会儿',
      u'嘀咕 嘟囔',
      u'抵达 到达 到了',
      u'抵用 抵押 抵换',
      u'点播 点歌',
      u'点击 按 按了 点了',
      u'电话 电话机 固话 固定电话',
      u'电脑 笔记本 笔记本电脑 IPAD 平板电脑',
      u'电视 电视机',
      u'订单 订单号',
      u'定位 定位导航',
      u'定制 订制',
      u'丢失 丢 丢了 掉 掉了 丢掉 找不到 找不着 没找到',
      u'短号 短码',
      u'短信 短信包',
      u'断网 断线 断开 上不了网 不能上网 断 上不去 连不上 上不去网 上网不畅',
      u'对面 对门',
      u'兑换券 兑换码',
      u'多少 几',
      u'儿童 小孩 小孩子 小学生 儿子 女儿',
      u'发送 收发',
      u'发图 发图片',
      u'反馈 回馈',
      u'反应 反映',
      u'返还 返 返给',
      u'返现 返款 返费 返钱',
      u'飞享套餐 飞享',
      u'飞信 飞信号',
      u'非要 非得',
      u'费用 价格',
      u'封锁 封停',
      u'符合 符合条件 符合要求',
      u'父母 父亲 母亲 爸妈 妈妈 爸爸 爸爸妈妈 爸 妈 我爸 我妈',
      u'副卡 副号 附号 附卡',
      u'覆盖 网络覆盖',
      u'改回 改回来',
      u'改少 改小',
      u'干嘛 干吗 干什么',
      u'刚刚 刚才 刚',
      u'港澳台 港澳',
      u'高级 高端',
      u'搞不定 搞不懂 搞不清',
      u'告诉 告知',
      u'歌曲 歌',
      u'个人信息 个人资料',
      u'更改 改改 改成 转成 改下 换下 修改 改为 改 变更 改掉 更换 改个 替换 转换成 转换 想改 想换 要换 替代 兑换 对换 兑 换换 换 换个 可换 可改 可兑换 可对换',
      u'更加 更',
      u'工行 工商银行',
      u'工作 上班',
      u'工作人员 工作者 工人',
      u'工作日 工作日内',
      u'公交 公交车',
      u'沟通 交流',
      u'购买 购 买 已购已买 购入',
      u'购物 买东西',
      u'顾客 买家',
      u'关闭 关掉 关了 退掉 关停 关一关 删掉 退个 关 推出 撤掉 终止 停止 销 停网 注销 注消 解除 停 停用 停掉 关上 取消 撤单 退除 去掉 停下 关下 能关 停止使用',
      u'观察 观望',
      u'规定 规则 使用规则',
      u'过期 失效',
      u'过时 过气',
      u'好友 朋友 同学 同事 哥们 盆友 小伙伴 朋友们 盆友们 学校同学',
      u'号码 号',
      u'何时 什么时候',
      u'核算 核对 核实',
      u'很多 好多 好多好多 较多 非常多 太多 许多 蛮多 比较多 不少 超多',
      u'很慢 慢 非常慢',
      u'很强 好强 非常强',
      u'很弱 好弱 非常弱',
      u'很少 好少 好少好少 较少 非常少 太少 蛮少 比较少 不多 超少',
      u'后面 后边',
      u'忽然 突然',
      u'话单 详单 话费单 明细 账务 帐务 账单 业务费 明细账单 账单明细',
      u'话费 通话费 通讯费 通信费 电话费 手机费',
      u'话费券 元宝券',
      u'缓冲 缓存',
      u'换回 换回来 换取',
      u'换机 换手机',
      u'恢复 恢复过来 恢复正常 重开',
      u'回事 回事儿',
      u'获得 获奖 获赠 赚取 赚 挣 攒 索取 得到 索要',
      u'积分 和积分',
      u'基本 基本上',
      u'即时 马上 立刻 当即 立马 即刻 即可',
      u'急用 急需',
      u'集团业务 集团网 集团V网 集团号 集团V套餐 集团V业务 集团 集团V 集团V网组',
      u'几百 几百块',
      u'几毛 几毛钱',
      u'几人 几个人 多少人',
      u'几月 几月份',
      u'几兆 多少兆',
      u'计费 收费 要钱 收钱',
      u'计算 算下 算',
      u'继续 接着',
      u'寄来 寄过来 寄到 寄回',
      u'加不进 加不上 加不了 不能加',
      u'加进来 加进去',
      u'家庭业务 家庭网 家庭 家庭网络 家庭V网 家庭号',
      u'家园网 家园卡',
      u'监控 监听',
      u'检查 检测 检修 来修',
      u'减少 减',
      u'将近 接近',
      u'奖品 奖励',
      u'交行 交通银行',
      u'缴费 交话费 充话费 付款 交费 掏钱 出钱 交 缴 冲 充 付 充了 冲了 充的 冲的 刚冲 刚充 付钱 付费 冲话费 充值 交钱 缴纳 交纳 上冲',
      u'接收 接到',
      u'接听 接听电话',
      u'接通 打通',
      u'结算 结账 结余',
      u'截止 截至',
      u'解绑 解除掉 解除绑定',
      u'解冻 解卡 解锁',
      u'解决 解决问题 弄 处理',
      u'解释 解释一下',
      u'今天 今儿 今儿个',
      u'尽快 赶快',
      u'进不去 进不来 进不了',
      u'进来 进入',
      u'进展 进度',
      u'近期 近月 近几个月',
      u'经常 时常 时不时 经常性 动不动',
      u'居然 竟然',
      u'具体操作 具体步骤',
      u'卡顿 都卡 很卡 非常卡',
      u'开心 高兴',
      u'看不出 看不见 看不着',
      u'看见 见到',
      u'科研 科学 科技',
      u'可能 也许 或许',
      u'可以 能 可',
      u'口令 口号 口令卡',
      u'扣费 扣 扣掉 扣钱 扣除',
      u'快速 快',
      u'宽带 移动宽带 有线宽带 家庭宽带 宽带E 宽带网',
      u'老年 老年人 老人 老人家',
      u'老用户 老客户',
      u'礼物 礼盒 礼品 礼包 礼券',
      u'里面 里边 里头 内 里',
      u'立刻生效 今天生效 马上生效 立马生效 立即生效 即刻生效',
      u'例如 举例 举个例子 举栗 举个栗子 比如 比如说',
      u'链接 连上 连 连接网络',
      u'两城一号 两城一家 两城一卡',
      u'两个 俩 俩个 两三个 两台 两只 两位 两张 两条 两款',
      u'聊天 聊聊 聊过',
      u'铃声 铃音',
      u'零首充 零首付 零首冲',
      u'领取 领 领用 领回来 领来 领到 领点 领奖',
      u'另外 额外',
      u'另一个 另一半',
      u'流量 流泪 流浪 兆 m',
      u'流量包 流量套餐 流量卡套餐 安心包 安心流量包 通用流量 通用流量包 香蕉',
      u'流水 流水号',
      u'乱收 乱收费',
      u'旅游 旅行',
      u'吗 嘛',
      u'买票 购票',
      u'买一送一 买一赠一 买1送1',
      u'满足 满足条件',
      u'慢慢 慢点',
      u'没费 没钱',
      u'没用 没有用 没有使用 没上 没有上',
      u'没有 木有 无 没 未',
      u'每日一笑 每曰一笑',
      u'每月 月月 每个月',
      u'妹子 妹纸 妹儿 妹妹',
      u'咪咕 咪咕会员 咪古',
      u'密码 登陆密码 登录密码 密钥 密令 密码保护 密码锁',
      u'免费 不要钱 0元 零元 免费送',
      u'免流 免流量',
      u'莫名 莫名奇妙 无故 无缘无故',
      u'目前 日前',
      u'哪个 哪种 哪款 哪只',
      u'哪里 哪儿 哪 什么地方 哪里面 什么位置 哪个位置 哪个地方 啥地方 啥位置 哪边',
      u'哪天 哪一天',
      u'哪位 谁',
      u'哪些 哪几种 哪几个',
      u'那个 那种 那款 那只',
      u'那里 那边 那儿',
      u'男朋友 男票 男盆友',
      u'能否 能不能 可否 可不可 可不可以',
      u'您 你',
      u'农信 农信通',
      u'农行 农业银行',
      u'女朋友 女票 女盆友',
      u'判断 评定',
      u'平时 平常',
      u'评价 评论',
      u'苹果 苹果机 IPHONE IPHONE5 IPHONE5S 5S 苹果手机',
      u'屏蔽 屏蔽掉',
      u'前段 前段时间 前两天 前不久',
      u'强行 强制',
      u'亲情号码 亲情号',
      u'亲情网 亲情业务',
      u'亲友 亲人 亲朋好友 家人',
      u'清楚 清晰',
      u'清零 清0 清空',
      u'情况 状况 情形',
      u'区别 区分',
      u'去年 上年',
      u'缺失 缺少 不完整 漏',
      u'确定 确认',
      u'热线 热线电话',
      u'人工服务 人工',
      u'仍然 依然 仍旧',
      u'如果 假如',
      u'入网 入户',
      u'删除 不要 抹除 剔除 删',
      u'擅自 私自',
      u'商城 商场',
      u'商户 卖家',
      u'商务 商贸 商盟',
      u'上门 上门服务 上门来',
      u'上网 联网 连网',
      u'上月 上一个月 上个月',
      u'上周 上星期 上个星期',
      u'设置 设 重置 设定 设为',
      u'申诉 控诉 投诉',
      u'身份证 身份证号 身分证',
      u'什么 啥 神马 何',
      u'神州行 神周行 神州',
      u'审核 审判 审查',
      u'升级 升 提升 升为 升档 生成',
      u'生效 申效 起效',
      u'声明 澄清 申明',
      u'省用 省钱 省点',
      u'剩余 剩 余 剩下 余下 遗留 留下',
      u'失败 发送失败 发不出去 充不进去 发不了 收发不了 不能收发',
      u'失误 按错 弄错',
      u'师傅 师父',
      u'时 时候',
      u'时好时坏 时有时无',
      u'时间 日期 年月',
      u'实名 实名制 实名认证',
      u'使得 使',
      u'使用 用 上用 用掉 用出去',
      u'事情 事儿 事',
      u'事物 事件',
      u'试用 试听 试试 试试看 试了 试过 试',
      u'是否 是不是 会不会',
      u'适合 适应 适用 合适',
      u'收到 发来',
      u'收取 收',
      u'手机号 手机号码',
      u'售卖 卖 出售 有的卖 售 销售',
      u'数据 数据包',
      u'数据服务 数据业务',
      u'数据网 数据网络',
      u'刷新 刷',
      u'说 讲',
      u'四月 四月份',
      u'速度 多快 速率 网速',
      u'算了 算了吧',
      u'算在 算到 算在内 算在里面',
      u'锁定 锁',
      u'他人 他机',
      u'套餐 套餐里',
      u'特别 尤其',
      u'特级 特种',
      u'提示 提醒',
      u'填写 填',
      u'听到 听见',
      u'投递 妥投',
      u'退出 退出来',
      u'退还 退钱 退费 退款 退订 推定 退下来 退到 退单 退',
      u'退回 退给 退回来 退回去',
      u'玩意 玩意儿',
      u'玩游戏 打游戏',
      u'网费 上网费',
      u'网银 网上银行',
      u'忘记 记不清 记不得 记不得了 忘 遗忘',
      u'微信 微信号',
      u'为何 为啥 为什么 为毛',
      u'违规 违章',
      u'尾数 尾号',
      u'未到账 没到账 只到账 不到账 没有到账',
      u'我 我家 俺家 俺 老子',
      u'无限 不限',
      u'无需 无须 不需要',
      u'五一 不小心 无意间',
      u'五月 五月份',
      u'误操作 误删 误点 误用 误收 误定 误关',
      u'下降 降 降到',
      u'下月 次月 下月初 下个月 下一月 过月',
      u'下周 下星期 下个星期',
      u'乡情网 乡情 相亲网 乡村 乡村网 乡村套餐',
      u'相同 同',
      u'详情 详细信息 详细情况',
      u'享受 享有 享用 享',
      u'像 如',
      u'消掉 消灭 消消',
      u'消费 花费 花了 花销 用了 款 花钱',
      u'销户 消户 报停 停机 挺号 退网',
      u'携带 带 携 携入',
      u'新装 新开 新开通 新安装 新买',
      u'信号 手机信号 网络信号',
      u'信任 相信',
      u'信息中心 信息办',
      u'信用 信用度 信誉 信誉度',
      u'星级 星',
      u'星期天 星期日 礼拜天',
      u'行不行 行么 行吗',
      u'修理 维修 修复 修',
      u'需要 需 须',
      u'续约 包了 续费 续订 续用 续交 续',
      u'选择 选用 选定 选号 选好 选 选中',
      u'寻找 找 找一下',
      u'延时 延期 延长 延续',
      u'摇奖 摇一摇 摇摇',
      u'夜话无眠 夜话',
      u'夜间流量 夜间包 夜间流量包',
      u'一个 一笔 一箱 一项 一遍 一部 一盒 一只 一条 一把 一所 一台 一件 一包',
      u'一卡多号 一卡双号',
      u'一元一天 一天一块 一天扣一块 一天扣一元',
      u'移动 中国移动',
      u'移动梦网 梦网',
      u'已办 已办理 已开 已开通',
      u'异常 非正常',
      u'异地 外地 省外 出省 外省',
      u'银行卡 银联卡',
      u'应用 应用程序',
      u'营业厅 营业点',
      u'用不完 用不掉 用不上 没用完 没有用完',
      u'优惠 优惠政策 优惠活动 优惠价 特惠 打折 便宜 实惠',
      u'优惠券 优惠卷',
      u'邮件 电邮 电子邮件',
      u'邮政 邮政储蓄',
      u'游戏 手游 手机游戏',
      u'有何 有什么',
      u'有没有 有木有',
      u'有时 有时候',
      u'有线 有线网',
      u'预付 预付费 预付款',
      u'预计 估计',
      u'预约 预定 订 定 已定',
      u'遇到 遇见 遇',
      u'元 块 块钱 元钱',
      u'原来 原先',
      u'原因 缘由 缘故 理由',
      u'月底 本月底 月末',
      u'月费 包月费',
      u'月消费 月话费',
      u'月租 月租费',
      u'允许 同意',
      u'在哪 在哪里',
      u'在线 线上',
      u'造成 导致',
      u'怎么 怎样 怎样才能 怎么才能 肿么 如何 怎么样 咋 哪样 怎',
      u'怎么办 怎办 咋办 咋整 咋弄',
      u'增加 多定 多包 多点 多充 多些 多冲 多一些 多一点 增强 增添 增',
      u'赠送 送 赠 互送 赠送给 馈赠 互赠 转让 转给 送给',
      u'诈骗 骗子 骗人 骗',
      u'掌厅 掌上营业厅 手机营业厅 网上营业厅 网厅 掌上移动厅 掌上客户端 掌上',
      u'账户 账面 帐户 账号 用户名',
      u'找回 找回来',
      u'真伪 真假',
      u'政务通 政企通 政企一卡通 政务一卡通',
      u'政务网 政府网',
      u'之后 后',
      u'知道 晓得',
      u'只限 只能 只给',
      u'指令 指令码',
      u'中信 中信银行',
      u'中行 中国银行',
      u'种类 品种',
      u'重启',
      u'重新 从新',
      u'重新加入 重新组建 重加',
      u'重新启动',
      u'抓小鸡 捉小鸡',
      u'专属 专有 专用 专享',
      u'转移 转 移 赚到 迁 迁移 牵走 移机 想迁 迁回 想移 移迁 移户 结转 转过来 转结 转过',
      u'转增 转增给',
      u'咨询 问 质询 问个 询问 请教',
      u'总公司 总店',
      u'总计 总额 累计 累积 总共 合计 累积到 累加 积',
      u'最低 最低价',
      u'昨天 昨儿',
      u'做什么 做啥',
      ]
    usrdict=[
      u'0元',
      u'2G',
      u'4G卡',
      u'5S',
      u'E币',
      u'M-FREE',
      u'M币',
      u'M值',
      u'PIK码',
      u'PIM码',
      u'PIN码',
      u'PLN码',
      u'PUK码',
      u'Q币',
      u'SIM卡',
      u'USIM卡',
      u'WI-FI',
      u'WIFE',
      u'爱奇艺',
      u'按错 v',
      u'按月',
      u'半年包',
      u'包时',
      u'包时套餐费',
      u'包天',
      u'包月',
      u'本号',
      u'本号码',
      u'本机',
      u'本机 n 1000',
      u'本月',
      u'比较多',
      u'比较少',
      u'变不变',
      u'变少 v 30',
      u'不成功',
      u'不错过',
      u'不到账 v',
      u'不掉',
      u'不对',
      u'不可以',
      u'不能加',
      u'不能上网 v',
      u'不能使用',
      u'不能收发 v',
      u'不能用',
      u'不上',
      u'不完整',
      u'不稳定',
      u'不限',
      u'不小心',
      u'不需要',
      u'不要钱',
      u'不用',
      u'不用了',
      u'不正确',
      u'不知道 v',
      u'不准 a',
      u'不准确 a',
      u'财付通',
      u'彩玲',
      u'彩铃库',
      u'蹭取 v',
      u'查一查 v',
      u'超快',
      u'超慢',
      u'冲话费 v',
      u'充不进去',
      u'充话费 v',
      u'充值券 v',
      u'抽中 v',
      u'出省 v',
      u'此号码',
      u'次月',
      u'打不通 v',
      u'代付 v',
      u'代付费',
      u'单品',
      u'倒是',
      u'到了 v',
      u'到帐 v',
      u'到账 v',
      u'登陆密码',
      u'登录密码',
      u'掉线 v',
      u'断网 v',
      u'兑换码',
      u'多大',
      u'多方通话',
      u'多快',
      u'多少人',
      u'多少兆',
      u'发不出去',
      u'发送失败',
      u'发信息 v',
      u'反倒是',
      u'返款 v',
      u'飞享',
      u'飞信号',
      u'非常多',
      u'非常卡',
      u'非常慢',
      u'非常强',
      u'非常弱',
      u'非常少',
      u'分钟数',
      u'付钱 v',
      u'副卡',
      u'覆盖点',
      u'个人热点',
      u'更改 v',
      u'功能费',
      u'固定电话',
      u'固话',
      u'归属地',
      u'过月',
      u'还能',
      u'好不好',
      u'好强',
      u'好弱',
      u'号码薄',
      u'合约机',
      u'合约期',
      u'和包',
      u'很多',
      u'很慢',
      u'很少',
      u'互送 v',
      u'花了 v',
      u'华谊兄弟',
      u'话费券',
      u'坏了 v',
      u'换手机 v',
      u'黄钻',
      u'会不会',
      u'即可生效 v',
      u'几个人',
      u'几人',
      u'季包',
      u'加不了 v',
      u'加不上 v',
      u'加油包',
      u'较多',
      u'接不到 v',
      u'截屏 v',
      u'解绑 v',
      u'解除绑定 v',
      u'解除掉 v',
      u'今天生效 v',
      u'禁查 v',
      u'举个例子 v',
      u'举个栗子 v',
      u'卡密',
      u'可办理',
      u'可不可',
      u'可不可以',
      u'可选费',
      u'扣费 v',
      u'扣扣',
      u'蓝钻',
      u'老年机',
      u'老用户',
      u'了啊',
      u'了吧',
      u'立刻生效 v',
      u'立马生效 v',
      u'连不了 v',
      u'连不了网 v',
      u'连不上 v',
      u'连不上网 v',
      u'连接网络 v',
      u'两城一卡',
      u'两个月',
      u'靓号',
      u'另一个',
      u'流量卡套餐',
      u'流量套餐',
      u'绿钻',
      u'马上生效 v',
      u'买1送1',
      u'买东西',
      u'买一赠一 v',
      u'蛮多',
      u'蛮少',
      u'没到 v',
      u'没到账 v',
      u'没法用',
      u'没上 v',
      u'没收到 v',
      u'没用完 v',
      u'没有到账 v',
      u'没有上 v',
      u'没有使用 v',
      u'没有用 v',
      u'没找到 v',
      u'每个月',
      u'每曰一笑',
      u'魅蓝',
      u'梦网',
      u'咪古',
      u'免流 v 10',
      u'免流量',
      u'免流量 v 10',
      u'明细账单',
      u'哪个地方',
      u'哪个位置',
      u'哪里面',
      u'哪种',
      u'能不能',
      u'能用',
      u'年月',
      u'苹果手机',
      u'欠费 v',
      u'清0 v',
      u'全号',
      u'全家桶',
      u'日版',
      u'融合型',
      u'三码合一',
      u'啥地方',
      u'啥都',
      u'啥位置',
      u'啥也',
      u'闪退 v',
      u'商品街',
      u'上不了网 v',
      u'上不去 v',
      u'上不去网 v',
      u'上个月',
      u'上网不畅 v',
      u'上网费',
      u'上一个月',
      u'上月',
      u'什么地方',
      u'什么都',
      u'什么时候',
      u'什么位置',
      u'什么也',
      u'时长',
      u'使用规则',
      u'世界电信日',
      u'是不是',
      u'收不到 v',
      u'收发不了',
      u'收钱',
      u'手机端',
      u'手机号',
      u'手机营业厅',
      u'手机游戏',
      u'手游',
      u'算不算',
      u'随身WIFI',
      u'他机',
      u'太多',
      u'套餐费',
      u'套餐外',
      u'特别卡',
      u'特惠包',
      u'剔除 v',
      u'替别人',
      u'替人',
      u'停复机',
      u'停号 v',
      u'停网 v',
      u'通话中',
      u'退出来 v',
      u'退还 v',
      u'妥投 v',
      u'挖宝箱 v',
      u'玩不起',
      u'网络信号',
      u'网内长市',
      u'网盘',
      u'网上营业厅',
      u'网速 n 100',
      u'网厅',
      u'网银',
      u'往上',
      u'微信',
      u'微信号',
      u'为毛',
      u'未到账 v',
      u'未接电话',
      u'我买网',
      u'无法使用',
      u'希望',
      u'下一月',
      u'下月',
      u'下月生效 v',
      u'线上',
      u'线下',
      u'详单',
      u'协议期',
      u'新入网',
      u'新用户',
      u'行不行',
      u'醒来 100',
      u'悬浮窗',
      u'炫铃',
      u'验证码',
      u'摇一摇',
      u'要不要',
      u'业务包',
      u'夜间包',
      u'夜间流量包',
      u'一个月',
      u'一加一',
      u'一天扣一块',
      u'一天扣一元',
      u'一天一块',
      u'一元一天',
      u'移户 v',
      u'移机 v',
      u'移迁 v',
      u'已办',
      u'已办理',
      u'已开',
      u'已开通',
      u'用不了',
      u'用出去 v',
      u'用掉 v',
      u'用户名',
      u'用来 v',
      u'用完',
      u'优惠券',
      u'有没有',
      u'有木有',
      u'有问题',
      u'有用',
      u'余额宝',
      u'语音包',
      u'元宝券',
      u'月月',
      u'越来越',
      u'在不在',
      u'在吗',
      u'在哪里',
      u'早晚报',
      u'怎么回事',
      u'掌上客户端',
      u'掌上营业厅',
      u'掌厅',
      u'账单明细',
      u'找不到 v',
      u'找回来 v',
      u'这个月',
      u'这条',
      u'这月',
      u'真的假的',
      u'中国移动',
      u'抓不到 v',
      u'转成 v',
      u'转过来 v',
      u'子号码',
      u'自办厅',
      u'做啥',
      u'做什么',
      ]
