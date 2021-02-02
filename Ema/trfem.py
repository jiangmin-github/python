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
    [7] row[19] assigndscrpt：利润分配
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
    [8] row[11] sumasset:总资产（元）
    [9] row[12] fixedasset:固定总资产（元）
    [10] row[13] monetaryfund:货币资金（元）
    [11] row[15] accountrec:应收账款（元）
    [12] row[17] inventory:库存（元）
    [13] row[19] sumliab:总负债（元）
    [14] row[20] accountpay:应付账款（元）
    [15] row[22] advancereceive:预收账款（元）
    [16] row[24] sumshequity:股东权益合计（元）
    [17] row[30] cashanddepositcbank:现金及银行存款（元）
    [18] row[32] loanadvances:贷款及垫付（元）
    [19] row[34] saleablefasset:可出售资产(元）
    [20] row[36] borrowfromcbank:银行借款（元）
    [21] row[38] acceptdeposit:接受存款(元）
    [22] row[40] sellbuybackfasset:出售回购资产(元)
    [23] row[42] settlementprovision:结算准备金（元）
    [24] row[44] borrowfund:借款资金（元）
    [25] row[46] agenttradesecurity:代理贸易担保(元)
    [26] row[48] premiumrec:优质记录（元）
    [27] row[50] stborrow:st借款（元）
    [28] row[52] premiumadvance:预付保费（元）

利润表
    [29] row[11] parentnetprofit：净利润
    [30] row[12] totaloperatereve：营业总收入（元）
    [31] row[13] totaloperateexp：营业总支出（元）
    [32] row[15] operateexp：营业支出（元）
    [33] row[17] saleexp：销售费用（元）
    [34] row[18] manageexp：管理费用（元）
    [35] row[19] financeexp：财务费用（元）
    [36] row[20] operateprofit：营业利润（元）
    [37] row[21] sumprofit：利润总额（元）
    [38] row[22] incometax：所得税（元）
    [39] row[28] operatetax：营业税（元）

现金流量表
    [40] row[11] netoperatecashflow:经营性现金流量净额
    [41] row[13] salegoodsservicerec:销售额
    [42] row[15] employeepay:雇员工资
    [43] row[17] netinvcashflow:投资性现金流净额
    [44] row[19] invincomerec:投资收益
    [-] row[21] buyfilassetpay:购买资产支付
    [-] row[23] netfinacashflow:净财务现金流量
    [-] row[25] nicashequi
    [-] row[27] niclientdeposit
    [-] row[29] niloanadvances
    [-] row[31] intandcommrec
    [-] row[33] agentuwsecurityrec
    [-] row[34] invpay
    [-] row[36] cashequibeginning
    [-] row[38] cashequiending
    [-] row[40] premiumrec
    [-] row[42] indemnitypay
    [-] row[45] nideposit
'''

#-*-coding:utf-8-*-

import csv
import os
import time

file_path = 'D:\\data\\emsort'
os.chdir(file_path)

hrec = []
data1 = []
data5 = []
data6 = []
data7 = []

ct = [           [2009, 2], [2009, 3], [2009, 4],
      [2010, 1], [2010, 2], [2010, 3], [2010, 4],
      [2011, 1], [2011, 2], [2011, 3], [2011, 4],
      [2012, 1], [2012, 2], [2012, 3], [2012, 4],
      [2013, 1], [2013, 2], [2013, 3], [2013, 4],
      [2014, 1], [2014, 2], [2014, 3], [2014, 4],
      [2015, 1], [2015, 2], [2015, 3], [2015, 4],
      [2016, 1], [2016, 2], [2016, 3], [2016, 4],
      [2017, 1], [2017, 2], [2017, 3], [2017, 4],
      [2018, 1], [2018, 2], [2018, 3], [2018, 4],
      [2019, 1], [2019, 2], [2019, 3], [2019, 4],
      [2020, 1], [2020, 2], [2020, 3], [2020, 4]]


# ct = [[2010,2]]


# 设置财务报表种类
# (1-业绩报表；2-业绩快报表：3-业绩预告表；4-预约披露时间表；5-资产负债表；6-利润表；7-现金流量表)
tt = [1, 5, 6, 7]
# tt = [6]

dict_tables = {1: '业绩报表', 2: '业绩快报表', 3: '业绩预告表',
               4: '预约披露时间表', 5: '资产负债表', 6: '利润表', 7: '现金流量表'}

def formhd(d1,d5,d6,d7):

    hrec.append('yearquarter')

    # print('formhd',d1[0][0])
    
    # 字段B开始
    astr = d1[0][0].split(",")
    hrec.append(astr[6])
    hrec.append(astr[7])
    hrec.append(astr[14])
    hrec.append(astr[15])
    hrec.append(astr[16])
    hrec.append(astr[17])

    # 字段H开始
    astr = d5[0][0].split(",")
    hrec.append(astr[11])
    hrec.append(astr[12])
    hrec.append(astr[13])
    hrec.append(astr[15])
    hrec.append(astr[17])
    hrec.append(astr[19])
    hrec.append(astr[20])
    hrec.append(astr[22])
    hrec.append(astr[24])
    hrec.append(astr[30])
    hrec.append(astr[32])
    hrec.append(astr[34])
    hrec.append(astr[36])
    hrec.append(astr[38])
    hrec.append(astr[40])
    hrec.append(astr[42])
    hrec.append(astr[44])
    hrec.append(astr[46])
    hrec.append(astr[48])
    hrec.append(astr[50])
    hrec.append(astr[52])

    # 字段AC开始
    astr = d6[0][0].split(",")
    hrec.append(astr[11])
    hrec.append(astr[12])
    hrec.append(astr[13])
    hrec.append(astr[15])
    hrec.append(astr[17])
    hrec.append(astr[18])
    hrec.append(astr[19])
    hrec.append(astr[20])
    hrec.append(astr[21])
    hrec.append(astr[22])
    hrec.append(astr[28])

    # 字段AN开始
    astr = d7[0][0].split(",")
    hrec.append(astr[11])
    hrec.append(astr[13])
    hrec.append(astr[15])
    hrec.append(astr[17])
    hrec.append(astr[19])
    hrec.append(astr[21])
    hrec.append(astr[23])
    hrec.append(astr[25])
    hrec.append(astr[27])
    hrec.append(astr[29])
    hrec.append(astr[31])
    hrec.append(astr[33])
    hrec.append(astr[34])
    hrec.append(astr[36])
    hrec.append(astr[38])
    hrec.append(astr[40])
    hrec.append(astr[42])
    hrec.append(astr[45]) 

# 写入表头
# 方法1 借助csv包，最常用
def write_headers(scode):
    # print(scode,year,quarter)
    if not os.path.exists('{}.csv'.format(scode)):
        with open('{}.csv' .format(scode), 'a', encoding='utf_8', newline='') as f:
            # print(headers)  # 测试 ok
            writer = csv.writer(f)
            writer.writerow(hrec)

def write_table(scode, rb):

    # 写入文件方法1
    with open('{}.csv' .format(scode), 'a', encoding='utf_8', newline='') as f:
            w = csv.writer(f)
            w.writerow(rb)

def trfem(year, quarter, d1, d5, d6, d7):
    len1 = len(d1)
    len5 = len(d5)
    len6 = len(d6)
    len7 = len(d7)
    idx1 = 1
    idx5 = 1
    idx6 = 1
    idx7 = 1
    gn1 = False
    gn5 = False
    gn6 = False
    gn7 = False
    eof1 = False
    eof5 = False
    eof6 = False
    eof7 = False
    ocode = '999999'

    while (not eof1) or (not eof5) or (not eof6) or (not eof7) :
        recbuff = []
        astr1 = d1[idx1][0].split(",")
        astr5 = d5[idx5][0].split(",")
        astr6 = d6[idx6][0].split(",")
        astr7 = d7[idx7][0].split(",")

        if eof1 : astr1[0] = '000000'
        if eof5 : astr5[0] = '000000'
        if eof6 : astr6[0] = '000000'
        if eof7 : astr7[0] = '000000'

        scode = max(astr1[0], astr5[0], astr6[0], astr7[0])


        # print("****************************************************")
        # print("scode",scode)
        # print("year",year)
        # print("quarter",quarter)
        # print("idx1",idx1)
        # print("len1",len1)
        # print("idx5",idx5)
        # print("len5",len5)
        # print("idx6",idx6)
        # print("len6",len6)
        # print("idx7",idx7)
        # print("len7",len7)
        # print("astr1",astr1)
        # print("astr5",astr5)
        # print("astr6",astr6)
        # print("astr7",astr7)
        # print("code : ",scode,ocode)

        if scode == ocode :
            if scode == astr1[0] :
                if idx1 < len1 - 1 :
                    idx1 += 1
                else :
                    eof1 = True
            if scode == astr5[0] :
                if idx5 < len5 - 1 :
                    idx5 += 1
                else :
                    eof5 = True
            if scode == astr6[0] :
                if idx6 < len6 - 1 :
                    idx6 += 1
                else :
                    eof6 = True
            if scode == astr7[0] :
                if idx7 < len7 - 1 :
                    idx7 += 1
                else :
                    eof7 = True
            continue;

        gn1 = False
        gn5 = False
        gn6 = False
        gn7 = False

        write_headers(scode)

        recbuff.append('{}{:02d}'.format(year,quarter))

        if scode == astr1[0] :
            recbuff.append(astr1[6])
            recbuff.append(astr1[7])
            recbuff.append(astr1[14])
            recbuff.append(astr1[15])
            recbuff.append(astr1[16])
            recbuff.append(astr1[17])
            gn1 = True
        else :
            for i in range(6) :
                recbuff.append('-')

        if scode == astr5[0] :
            recbuff.append(astr5[11])
            recbuff.append(astr5[12])
            recbuff.append(astr5[13])
            recbuff.append(astr5[15])
            recbuff.append(astr5[17])
            recbuff.append(astr5[19])
            recbuff.append(astr5[20])
            recbuff.append(astr5[22])
            recbuff.append(astr5[24])
            recbuff.append(astr5[30])
            recbuff.append(astr5[32])
            recbuff.append(astr5[34])
            recbuff.append(astr5[36])
            recbuff.append(astr5[38])
            recbuff.append(astr5[40])
            recbuff.append(astr5[42])
            recbuff.append(astr5[44])
            recbuff.append(astr5[46])
            recbuff.append(astr5[48])
            recbuff.append(astr5[50])
            recbuff.append(astr5[52])
            gn5 = True
        else :
            for i in range(21) :
                recbuff.append('-')    

        if scode == astr6[0] :
            recbuff.append(astr6[11])
            recbuff.append(astr6[12])
            recbuff.append(astr6[13])
            recbuff.append(astr6[15])
            recbuff.append(astr6[17])
            recbuff.append(astr6[18])
            recbuff.append(astr6[19])
            recbuff.append(astr6[20])
            recbuff.append(astr6[21])
            recbuff.append(astr6[22])
            recbuff.append(astr6[28])
            gn6 = True
        else :
            for i in range(11) :
                recbuff.append('-')

        if scode == astr7[0] :
            recbuff.append(astr7[11])
            recbuff.append(astr7[13])
            recbuff.append(astr7[15])
            recbuff.append(astr7[17])
            recbuff.append(astr7[21])
            recbuff.append(astr7[19])
            recbuff.append(astr7[21])
            recbuff.append(astr7[23])
            recbuff.append(astr7[25])
            recbuff.append(astr7[27])
            recbuff.append(astr7[29])
            recbuff.append(astr7[31])
            recbuff.append(astr7[33])
            recbuff.append(astr7[34])
            recbuff.append(astr7[36])
            recbuff.append(astr7[38])
            recbuff.append(astr7[40])
            recbuff.append(astr7[42])
            recbuff.append(astr7[45])
            gn7 = True
        else :
            for i in range(18) :
                recbuff.append('-')

        write_table(scode, recbuff)
        # exit(2)

        if gn1 :
            if idx1 < len1 - 1 :
                idx1 += 1
            else :
                eof1 = True
        if gn5 :
            if idx5 < len5 - 1 :
                idx5 += 1
            else :
                eof5 = True
        if gn6 :
            if idx6 < len6 - 1 :
                idx6 += 1
            else :
                eof6 = True
        if gn7 :
            if idx7 < len7 - 1 :
                idx7 += 1
            else :
                eof7 = True

        ocode = scode 

        # print(idx1,len1,idx5,len5,idx6,len6,idx7,len7)
        # if idx1 == 4 :
        #    exit(3)

def reademfiles(year,quarter,d1,d5,d6,d7): 

    category = dict_tables[1]
    with open('{}-{}-{}.csv'.format(category,year,quarter), encoding='UTF-8') as f1 :
        rf1 = csv.reader(f1, delimiter='|')
        for row in rf1 :
            d1.append(row)

    category = dict_tables[5]
    with open('{}-{}-{}.csv'.format(category,year,quarter), encoding='UTF-8') as f5 :
        rf5 = csv.reader(f5, delimiter='|')
        for row in rf5 :
            d5.append(row)

    category = dict_tables[6]
    with open('{}-{}-{}.csv'.format(category,year,quarter), encoding='UTF-8') as f6 :
        rf6 = csv.reader(f6, delimiter='|')
        for row in rf6 :
            d6.append(row)

    category = dict_tables[7]
    with open('{}-{}-{}.csv'.format(category,year,quarter), encoding='UTF-8') as f7 :
        rf7 = csv.reader(f7, delimiter='|')
        for row in rf7 :
            d7.append(row)

    f1.close()
    f5.close()
    f6.close()
    f7.close()

    # print(d1)

if __name__ == '__main__':
    # i 按年度季度顺序处理
    for i in ct :
        data1 = []
        data5 = []
        data6 = []
        data7 = []
        reademfiles(i[0], i[1], data1, data5, data6, data7)
        # print(data1)
        if i[0] == 2009 and i[1] == 2 :
            formhd(data1, data5, data6, data7)

        print("Transforming ... ",i[0],i[1])
        trfem(i[0], i[1], data1, data5, data6, data7)
        # exit(1)
