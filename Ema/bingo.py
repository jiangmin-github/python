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


file_path = 'D:\\data\\emsort'
os.chdir(file_path)

#scode = input("Please input scode :")

filelist = os.listdir(file_path)
for fn in filelist :
    if fn[0:1] == '2' or fn[0:1] == '9' :
        continue
    # 毛利率指标计算变量
    mll = 0
    pjmll = 0
    num1 = 0
    # 资产收益率指标计算变量
    jzcsyl = 0
    pjjzcsyl = 0
    num2 = 0
    # 净利润指标计算变量
    jlr = 0
    pjjlr = 0
    num4 = 0
    oldjlr = 0
    jlrzz = True
    jlrzb = True
    # 营业总收入指标计算变量
    yyzsr = 0
    pjjyyzsr = 0
    num3 = 0


    with open(fn, encoding='UTF-8') as f :
        rf = csv.reader(f, delimiter=',')
        for row in rf :
            if row[0][4:] == '04' :
                if row[3] != '-' :
                    try:
                        jzcsyl += float(row[3])
                    except ValueError:
                        print('scode = ', fn[0:6], 'row[3]')
                    num2 += 1
                if row[6] != '-' :
                    mll += float(row[6])
                    num1 += 1
                if row[28] != '-' :
                    if oldjlr != 0 and oldjlr > float(row[28]) :
                        jlrzz = False
                    oldjlr = float(row[28]) 
                    if row[29] != '-' :
                        jlr += float(row[28])
                        yyzsr += float(row[29])
                        if float(row[28]) * 4 <= float(row[29]) :
                            jlrzb = False
                        #if fn[0:6] == '600519' :
                        #    print(row[0][0:4])
                        #    print(jlr)
                        #    print(yyzsr)

    if num1 != 0 :
        pjmll = mll / num1
    if num2 != 0 :
        pjjzcsyl = jzcsyl / num2
    
    # 条件：平均毛利率 > 80 & 平均净资产收益率 > 30
    #if pjmll > 80 and pjjzcsyl > 30 :

    # 条件：平均资产收益率 > 40 & 净利润持续增长
    #if pjjzcsyl > 40 and jlrzz == True :

    jlr = jlr * 3
    #if fn[0:6] == '600519' :
    #    print(jlr)
    #    print(yyzsr)

    # 条件：平均资产收益率 > 40 & 净利润持续增长 & 净利润占总营收的比例持续超过25%
    if pjjzcsyl > 17 and jlrzz == True and jlrzb == True :
        print('scode = ', fn[0:6], 'mll = ', pjmll, 'jzcsyl = ', pjjzcsyl)