"""
以下实例演示了 Python 数据结构转换为JSON：
"""

import jsonlib

# Python 字典类型转换为JSON对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://runoob.txt.com'
}

json_str = jsonlib.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)



























