import urllib.request as urt
import jsonlib
from html.parser import HTMLParser


"""
面给出的例子抽取了html中的所有链接：（在PYTHON3.3版本中）

handle_starttag( tag, attrs)
handle_startendtag( tag, attrs)
handle_endtag( tag)

来实现自己需要的功能。

tag是的html标签，attrs是 (属性，值)元组(tuple)的列表(list)。
HTMLParser自动将tag和attrs都转为小写。
"""


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "div":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "data-permalink-path":
                        self.links.append(value)


opener = urt.build_opener()  # urllib创建开启url器
# 设置头文件参数: User-agent, Cookie
opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like"
                                    " Gecko) Chrome/55.0.2883.87 Safari/537.36")]
opener.addheaders = [('Cookie', "guest_id=v1%3A148482531768369694;"
                                " mobile_metrics_token=148482538426969560;"
                                " zrca=5; lang=zh-cn; ct0=aa552011c9f355e710321a226"
                                "60b57a4; rsap=1; _mobile_sess=BAh7ByIKZmxhc2hJQzonQWN0"
                                "aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNoSGFzaHsABjoKQHVzZWR"
                                "7ADoQX2NzcmZfdG9rZW4iJTViMjY1NTAwMmQzYjc5MDk5ZTUyMjg2ZDRm"
                                "ODRlMzI1--d47c9fabb6613c0b8a0e6c8d54e31ae533dc631a; kdt=um9U"
                                "DXk2qUARHElvAh5qyd7unesk6QvMLYPverbd; remember_checked_on=1;"
                                " twid=\"u=819088284554907648\"; auth_token=b6c16e8edae3cd837c4d" \
                                "dc852beaca3983cb79dd; _gat=1; pid=\"v3:1485005157867089487330464\";" \
                                " _ga=GA1.2.1762403604.1484825327; _twitter_sess=BAh7CiIKZmxhc2hJ" \
                                 "QzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFza"
                                "HsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCLSVHcBZAToMY3NyZl9p%250A"
                                "ZCIlNjI1M2ZmNWVhMWIxODdmMjVkYWMyNTJlZjM0N2ZhYjU6B2lkIiU4YzYw"
                                "%250ANzBjZGM5MDJmNjU2YTE5OGM1NzllNWVmZTA2YzoJdXNlcmwrCQBQlIB0%"
                                "252FF0L--b0a1b914a2bb8ee723147919341cb061406db899")]
page = opener.open("https://twitter.com/poke/likes/timeline?include_available_features=1&"
                   "include_entities=1"
                   "&max_position=818703439244902402&reset_error_state=false", data=None,
                   timeout=100)
content = page.read()  # 读取response文件
print("content:", content)
# 将response文件转换成JSON格式，JSON转换成Python字典数据结构
data = jsonlib.loads(content)
print("data:", data)
# 获取字典数据结构内部的数据字段和值(key: value) new_latent_count":20
# 转换str to int
min_position = int(data['min_position'])
mobile_id = min_position - 1
mobile_id = str(mobile_id)
print("mobile_id:", mobile_id, ", type:", type(mobile_id))
print("min_position:", min_position, ", type:", type(min_position))
print("has_more_items:", data['has_more_items'])
print("new_latent_count:", data['new_latent_count'])  # int
# print("items_html:", data['items_html'])
items_html = data['items_html']
hp = MyHTMLParser()
hp.feed(items_html)
hp.close()
print("links:", hp.links)
print("size-links:", len(hp.links))
# 把list中的所有URL(相对地址)转换成绝对地址
for i in hp.links:
    str_absolute_URL = "https://twitter.com"+i
    print("str_absolute_URL:", str_absolute_URL)
