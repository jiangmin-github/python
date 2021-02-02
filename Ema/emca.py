"""
e.g: http://data.eastmoney.com/bbsj/201806/lrb.html
"""
import requests
import re
from multiprocessing import Pool
import json
import csv
import pandas as pd
import os
import time

# 设置文件保存在D盘eastmoney文件夹下
file_path = 'D:\\eastmoney'
if not os.path.exists(file_path):
    os.mkdir(file_path)
os.chdir(file_path)

'''
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
      [2020, 1]]
'''

ct = [[2020,3],[2020,4]]


# 设置财务报表种类
# (1-业绩报表；2-业绩快报表：3-业绩预告表；4-预约披露时间表；5-资产负债表；6-利润表；7-现金流量表)
tt = [1, 2, 3, 4, 5, 6, 7]
#tt = [7]

# 1 设置表格爬取时期
def set_table(y1, q1, t1):

    year = y1
    quarter = q1
    tables = t1

    # 转换为所需的quarter 两种方法,2表示两位数，0表示不满2位用0补充，
    # http://www.runoob.com/python/att-string-format.html
    quarter = '{:02d}'.format(quarter * 3)
    # quarter = '%02d' %(int(month)*3)

    # 确定季度所对应的最后一天是30还是31号
    if (quarter == '06') or (quarter == '09'):
        day = 30
    else:
        day = 31
    date = '{}-{}-{}' .format(year, quarter, day)
    # print('date:', date)  # 测试日期 ok

    dict_tables = {1: '业绩报表', 2: '业绩快报表', 3: '业绩预告表',
                   4: '预约披露时间表', 5: '资产负债表', 6: '利润表', 7: '现金流量表'}

    dict = {1: 'YJBB', 2: 'YJKB', 3: 'YJYG',
            4: 'YYPL', 5: 'ZCFZB', 6: 'LRB', 7: 'XJLLB'}
    category = dict[tables]

    # js请求参数里的type，第1-4个表的前缀是'YJBB20_'，后3个表是'CWBB_'
    # 设置set_table()中的type、st、sr、filter参数
    if tables == 1:
        category_type = 'YJBB20_'
        st = 'latestnoticedate'
        sr = -1
        filter =  "(securitytypecode in ('058001001','058001002'))(reportdate=^%s^)" %(date)
    elif tables == 2:
        category_type = 'YJBB20_'
        st = 'ldate'
        sr = -1
        filter = "(securitytypecode in ('058001001','058001002'))(rdate=^%s^)" %(date)
    elif tables == 3:
        category_type = 'YJBB20_'
        st = 'ndate'
        sr = -1
        filter=" (IsLatest='T')(enddate=^2018-06-30^)"
    elif tables == 4:
        category_type = 'YJBB20_'
        st = 'frdate'
        sr = 1
        filter =  "(securitytypecode ='058001001')(reportdate=^%s^)" %(date)
    else:
        category_type = 'CWBB_'
        st = 'noticedate'
        sr = -1
        filter = '(reportdate=^%s^)' % (date)

    category_type = category_type + category
    # print(category_type)
    # 设置set_table()中的filter参数

    yield{
    'date':date,
    'category':dict_tables[tables],
    'category_type':category_type,
    'st':st,
    'sr':sr,
    'filter':filter
    }

# 3 表格正式爬取
def get_table(date, category_type,st,sr,filter,page):
    # 参数设置
    params = {
        # 'type': 'CWBB_LRB',
        'type': category_type,  # 表格类型
        'token': '70f12f2f4f091e459a279469fe49eca5',
        'st': st,
        'sr': sr,
        'p': page,
        'ps': 50,  # 每页显示多少条信息
        'js': 'var LFtlXDqn={pages:(tp),data: (x)}',
        'filter': filter,
        # 'rt': 51294261  可不用
    }
    url = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?'

    # print(url)
    try:
        response = requests.get(url, params=params).text
    except requests.exceptions.RequestException as e:
        print(e)

    # print(response)
    # exit(0)


    # 确定页数
    pat = re.compile('var.*?{pages:(\d+),data:.*?')
    page_all = re.search(pat, response)
    print(page_all.group(1))  # ok

    # 提取{},json.loads出错
    # pattern = re.compile('var.*?data: \[(.*)]}', re.S)

    # 提取出list，可以使用json.dumps和json.loads
    pattern = re.compile('var.*?data: (.*)}', re.S)
    items = re.search(pattern, response)
    # 等价于
    # items = re.findall(pattern,response)
    # print(items[0])
    data = items.group(1)
    data = json.loads(data)
    # data = json.dumps(data,ensure_ascii=False)

    return page_all, data, page

# 写入表头
# 方法1 借助csv包，最常用
def write_header(data,category,y2,q2):
    with open('{}-{}-{}.csv' .format(category,y2,q2), 'a', encoding='utf_8_sig', newline='') as f:
        headers = list(data[0].keys())
        # print(headers)  # 测试 ok
        writer = csv.writer(f)
        writer.writerow(headers)

def write_table(data,page,category,y3,q3):
    print('\n正在下载{}-{}-{} 第 {} 页表格'.format(category,y3,q3,page))
    # 写入文件方法1
    for d in data:
        with open('{}-{}-{}.csv' .format(category,y3,q3), 'a', encoding='utf_8_sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(d.values())

def main(date, category_type,st,sr,filter,page,y4,q4):
    func = get_table(date, category_type,st,sr,filter,page)
    data = func[1]
    page = func[2]
    write_table(data,page,category,y4,q4)


if __name__ == '__main__':
    # i 报表类型
    for i in tt :
        # j 报表年-季
        for j in ct :
            for k in set_table(j[0],j[1],i):
                date = k.get('date')
                category = k.get('category')
                category_type = k.get('category_type')
                st = k.get('st')
                sr = k.get('sr')
                filter = k.get('filter')

                constant = get_table(date,category_type,st,sr,filter, 1)
                page_all = constant[0]

                start_page = 1
                end_page = int(page_all.group(1)) + 1

                # print(start_page, end_page)
                # exit(0)

                # 写入表头
                write_header(constant[1],category,j[0],j[1])
                start_time = time.time()  # 下载开始时间
                # 爬取表格主程序
                for page in range(start_page, end_page):
                    main(date,category_type,st,sr,filter,page,j[0],j[1])
    
                end_time = time.time() - start_time  # 结束时间
                print('下载完成')
                print('下载用时: {:.1f} s' .format(end_time))
