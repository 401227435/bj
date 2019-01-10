# -*- coding:utf-8 -*-
'''
@Author  : 庞朝文
@Time    : 2019/1/2 14:29 
@File    : t.py
@software: beijingcaigouwang
'''
import random
from fake_useragent import UserAgent
import requests
import json
import time
import re
ua = UserAgent().random
headers = {"User-Agent": ua}
url='http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/t20190102_1071413.html'
response=requests.get(url=url,headers=headers)
response=response.text

# 项目编号
# itemnum=re.findall('<strong>项目编号：</strong>(\S+)</p><p><strong>项目',response)[0]
itemnum=re.findall("<label for='type'>项目编号：</label>\n  </td>\n  <td colspan='3'>\n   (\S+)\n  </td>",response)[0]

# 项目联系人
responsible=re.findall('</strong></p><p>项目联系人：(\S+)</p><p>项目',response)

# 采购单位
# procurement=re.findall('采购单位：(\S+)</p>',response)
procurement=re.findall("<label for='type'>采购人(甲方)：</label>\n  </td>\n  <td colspan='3'>\n   北京世界园艺博览会事务协调局（本级）\n  </td>",response)

# 代理机构
Agency=re.findall('代理机构：(\S+)</p>',response)

# 代理人
responsible_person=re.findall('代理机构联系人：(\S+)</p><p>代',response)

# 预算金额
# amount=re.findall('预算金额：(\S+) 万元（人民币）</p>',response)
# amount=re.findall('(\S+) 万元（人民币）</p>',response)

amount=re.findall('(\S+)   万元',response)
# amount=re.findall("<label for='type'>合同金额：</label>\n  </td>\n  <td colspan='3'>\n(\S+)   万元\n   </c:if>\n  </td>",response)

# amount=float(amount[0])*10000
print(itemnum,responsible,procurement,Agency,responsible_person,amount)