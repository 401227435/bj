# -*- coding:utf-8 -*-
'''
@Author  : 庞朝文
@Time    : 2018/12/28 16:45 
@File    : test.py
@software: beijingcaigouwang
'''
import requests
import re
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
url = 'http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbgg/t20181228_1069283.html'
response = requests.get(url=url, headers=headers)
response = response.content.decode('gbk')
# print(response)


type=re.findall('&nbsp;([\u4E00-\u9FA5])+级招标公告</span>',response)[0]
title=re.findall('项目名称：</strong>([\u4E00-\u9FA5]+)</p>',response)[0]
num=re.findall('项目编号：</strong>(\S+)</p><p><strong>项目联',response)[0]
company=re.findall('采购单位：(\S+)?</p>',response)[0]
usre=re.findall('<p>采购用途：([\u4E00-\u9FA5]+)</p><p>',response)[0]
maney=re.findall('<p>预算金额：(\S+\s+\S+)（人民币）</p>',response)[0]
# <p>预算金额：86.48 万元（人民币）</p>
print(type+'级招标公告')
print(title)
print(num)
print(company)
print(usre)
print(maney)