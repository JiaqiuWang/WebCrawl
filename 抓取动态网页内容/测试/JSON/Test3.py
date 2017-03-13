"""
如果你要处理的是文件而不是字符串，你可以使用 json.dump()
和 json.load() 来编码和解码JSON数据。例如
"""

import jsonlib

# 写入文件
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://runoob.txt.com'
}

with open('data.json', 'w') as f:
    jsonlib.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = jsonlib.loads(f)























