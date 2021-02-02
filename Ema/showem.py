'''
业绩报表
    [1] row[06] basiceps：每股收益（元）
    [2] row[07] cutbasiceps：调整后每股收益（元）
    [ ] row[08] totaloperatereve：营业收入（元）
    [ ] row[09] ystz：营业收入同比增长
    [ ] row[10] yshz：营业收入季度环比增长
    [ ] row[11] parentnetprofit：净利润
    [ ] row[12] sjltz：净利润同比增长
    [ ] row[13] sjlhz：净利润环季度比增长
    [3] row[14] roeweighted：净资产收益率
    [4] row[15] bps：每股净资产（元）
    [5] row[16] mgjyxjje：每股经营现金流量（元）
    [6] row[17] xsmll：销售毛利率
    [ ] row[18] publishname：所处行业
    [ ] row[19] assigndscrpt：利润分配
    [ ] row[23] firstnoticedate：最新公告日期

业绩快报
    basiceps：每股收益（元）
    yysr：营业收入（元）
    ys：营业收入同比增长
    yshz：营业收入季度环比增长
    qntqys：营业收入去年同期
    jlr：净利润
    lr：净利润同比增长
    jlrhz：净利润环季度比增长
    qntqjlr：净利润去年同期
    roeweighted：净资产收益率
    parentbvps：每股净资产（元）
    publishname：所处行业
    firstnoticedate：最新公告日期

资产负债表
    [ ] row[04] publishname：所处行业
    [7] row[11] 总资产（元）
    [8] row[12] 固定总资产（元）
    [9] row[13] 货币资金（元）
    [10] row[15] 应收账款（元）
    [11] row[17] 库存（元）
    [12] row[19] 总负债（元）
    [13] row[20] 应付账款（元）
    [14] row[22] 预收账款（元）
    [15] row[24] 股东权益合计（元）
    [16] row[30] 现金及银行存款（元）
    [17] row[32] 贷款及垫付（元）
    [18] row[34] 可出售资产(元）
    [19] row[36] 银行借款（元）
    [20] row[38] 接受存款(元）
    [21] row[40] 出售回购资产(元)
    [22] row[42] 结算准备金（元）
    [23] row[44] 借款资金（元）
    [24] row[46] 代理贸易担保(元)
    [25] row[48] 优质记录（元）
    [26] row[50] st借款（元）
    [27] row[52] 预付保费（元）

利润表
    [28] row[11] parentnetprofit：净利润
    [29] row[12] totaloperatereve：营业总收入（元）
    [30] row[13] totaloperateexp：营业总支出（元）
    [31] row[15] operateexp：营业支出（元）
    [32] row[17] saleexp：销售费用（元）
    [33] row[18] manageexp：管理费用（元）
    [34] row[19] financeexp：财务费用（元）
    [35] row[20] operateprofit：营业利润（元）
    [36] row[21] sumprofit：利润总额（元）
    [37] row[22] incometax：所得税（元）
    [38] row[28] operatetax：营业税（元）

现金流量表
    [39] row[11] 经营性现金流量净额
    [40] row[13] 销售额
    [41] row[15] 雇员工资
    [42] row[17] 投资性现金流净额
    [43] row[19] 投资收益
    [-] row[21]
    [-] row[23]
    [-] row[25]
    [-] row[27]
    [-] row[29]
    [-] row[31]
    [-] row[33]
    [-] row[34]
    [-] row[36]
    [-] row[38]
    [-] row[40]
    [-] row[42]
    [-] row[45]
'''

#-*-coding:utf-8-*-

import csv
import os
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# sel = [0,1,3,4,5,6,8,9,10,11,12,13,14,15,16,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

dict_1 = {'basiceps':'每股收益',
        'cutbasiceps':'调整后每股收益',
        'roeweighted':'净资产收益率',
        'bps':'每股净资产',
        'mgjyxjje':'每股经营现金流量',
        'xsmll':'销售毛利率',
        'assigndscrpt':'利润分配',
        'sumasset':'总资产',
        'fixedasset':'固定总资产',
        'monetaryfund':'货币资金',
        'accountrec':'应收账款',
        'inventory':'库存',
        'sumliab':'总负债',
        'accountpay':'应付账款',
        'advancereceive':'预收账款',
        'sumshequity':'股东权益合计',
        'cashanddepositcbank':'现金及银行存款',
        'loanadvances':'贷款及垫付',
        'saleablefasset':'可出售资产',
        'borrowfromcbank':'银行借款',
        'acceptdeposit':'接受存款',
        'sellbuybackfasset':'出售回购资产',
        'settlementprovision':'结算准备金',
        'borrowfund':'借款资金',
        'agenttradesecurity':'代理贸易担保',
        'premiumrec':'优质记录',
        'stborrow':'st借款',
        'premiumadvance':'预付保费',
        'parentnetprofit':'净利润',
        'totaloperatereve':'营业总收入',
        'totaloperateexp':'营业总支出',
        'operateexp':'营业支出',
        'saleexp':'销售费用',
        'manageexp':'管理费用',
        'financeexp':'财务费用',
        'operateprofit':'营业利润',
        'sumprofit':'利润总额',
        'incometax':'所得税',
        'operatetax':'营业税',
        'netoperatecashflow':'经营性现金流量净额',
        'salegoodsservicerec':'销售额',
        'employeepay':'雇员工资',
        'netinvcashflow':'投资性现金流净额',
        'invincomerec':'投资收益'}


selist = [[0,2,4,5], 
          [0,3,6], 
          [0,7,8,9,10,11,12,13,15], 
          [0,28,29,30,31,35,36,37,38],
          [0,29,30,32,33,34],
          [0,28,39,40,41,42,43]]

xdata = []
ydata = []

file_path = 'D:\\data\\emsort'
os.chdir(file_path)

scode = input("Please input scode :")
while scode != '999999' :
    for k,sel in enumerate(selist) :
        num = len(sel)
        alist = [[] for _ in range(num)]
        with open('{}.csv'.format(scode), encoding='UTF-8') as f :
            rf1 = csv.reader(f, delimiter=',')
            for row in rf1 :
                for i,idx in enumerate(sel) :
                    alist[i].append(row[idx])    

        xname = alist[0][0]
        xdata = alist[0][1:]
     
        #ax = plt.subplot(m, 1, k + 1)
        plt.xticks(rotation=315)    

        for i in range(num - 1) :
            ydata = []
            yname = alist[i+1][0]
            ylist = alist[i+1][1:]
            for j,yd in enumerate(ylist) :
                if yd == '-' :
                    if j == 0 :
                        ydata.append(0)
                    else :
                        ydata.append(ydata[j-1])
                else :
                    ydata.append(float(yd))    

            # plt.xlabel(xname)
            # plt.ylabel(yname)
            
            plt.plot(xdata,ydata,marker='o',label='{}'.format(dict_1[yname]))
            plt.legend()
        plt.show()
    scode = input("Please input scode :")