# -*- coding:utf-8 -*-
'''
@Author  : 庞朝文
@Time    : 2018/12/28 15:00 
@File    : bj_caigou.py
@software: beijingcaigouwang
'''
import random
# from fake_useragent import UserAgent
import requests
import json
import time
import random
# from fake_useragent import UserAgent
import requests
import lxml
from lxml import etree
import json
import re
import time
# 中标 http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbjggg/index.html
# 采购 http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbgg/index.html

class BJCGW(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

        self.url='http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbgg/index.html'
        self.pre_url='http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbgg/'
    def get_url(self,url):
        response = requests.get(url=url, headers=self.headers)
        response = response.content.decode('gbk')
        return response

    def get_data_from_page(self,page):
        mytree = lxml.etree.HTML(page)
        data_list = []
        for tree in mytree.xpath('/html/body/ul/li'):
            data = {}
            data['url'] = 'http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbgg' + tree.xpath('./a/@href')[0][1:]
            data['title'] = tree.xpath('./a/text()')[0]
            data['date'] = tree.xpath('./span/text()')[0]
            data['t'] = self.get_detail_imgs_from_url(data['url'])
            data_list.append(data)
        nurl = mytree.xpath('//a[text()="下一页"]/@href')[0]

        # print(data_list)
        if len(nurl) !=0:
            nurl=self.pre_url+nurl
            print(nurl)
        else:
            nurl=None
        return data_list,nurl
    def get_detail_imgs_from_url(self,url):
        response = self.get_url(url)
        # 使用正则匹配
        # type = re.findall('&nbsp;([\u4E00-\u9FA5])+级招标公告</span>', response)[0]
        # title = re.findall('项目名称：</strong>([\u4E00-\u9FA5]+)</p>', response)[0]
        # num = re.findall('项目编号：</strong>(\S+)</p><p><strong>项目联', response)[0]
        # company = re.findall('采购单位：(\S+)?</p>', response)[0]
        # usre = re.findall('采购用途：([\u4E00-\u9FA5]+)</p><p>', response)#[0]<p>采购用途：施工图设计</p>
        # maney = re.findall('<p>预算金额：(\S+\s+\S+)（人民币）</p>', response)[0]
        # # <p>预算金额：86.48 万元（人民币）</p>
        # print(type + '级招标公告')
        # print(title)
        # print(num)
        # print(company)
        # print(usre)
        # print(maney)
        return 1

    def save_data(self):
        pass

    def run(self):
        url=self.url
        while url:

            print(url)
            page=self.get_url(url)
            data_list,url=self.get_data_from_page(page)
            # print(data_list)
            # self.save_data(data_list)
            time.sleep(0.2)

if __name__ == '__main__':
    bj=BJCGW()
    bj.run()