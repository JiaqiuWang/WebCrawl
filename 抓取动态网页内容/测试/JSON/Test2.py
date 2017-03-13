"""
将一个JSON编码的字符串转换回一个Python数据结构
"""

import jsonlib

data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://runoob.txt.com'
}

json_str = jsonlib.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)


# 将JSON对象转换为Python字典
data2 = jsonlib.loads(json_str)
print("data2['name']:", data2['name'])
print("data2['url']:", data2['url'])















