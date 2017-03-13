"""
使用Python 3抓取网页页面
urllib2在python3.x中被改为urllib.request
"""

import urllib.request as urt

url = "https://twitter.com/poke/with_replies"
up = urt.urlopen(url)  # 打开目标页面，存入变量up
cont = up.read()  # 从up中读入HTML文件
print("cont:", cont)
#
# key1 = '<a href = http'  # 设置关键字1
# key2 = "target"  # 设置管家机子2
#
# pa = cont.find(key1)  # 找出关键字1的位置
# pt = cont.find(key2, pa)  # 找出关键字2的位置(从字1后面开始查找)
#
# urlx = cont[pa:pt]  # 得到关键字1与关键字2之间的内容(即想要的数据).
# print("urlx:", urlx)
