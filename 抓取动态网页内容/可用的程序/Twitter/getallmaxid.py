"""
Name: 循环获取瀑布流网址的id参数
Author: Jia_qiu Wang(王佳秋)
Data: Jan, 2017
function:
"""

import time
import urllib.request as urt
import jsonlib


class ParseTimeFlowData:

    # 类的公有参数
    # list_all_next_cursor = []

    """构造函数"""
    def __init__(self, user_agent, cookie, url, filename):

        self.user_agent = user_agent
        self.cookie = cookie
        self.url = url
        self.filename = filename

    """析构函数"""
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "has Destroyed！")

# -------------------------------------------------------------------------------------------------------------------- #

    """循环获取min_position: 819772362837004291
              has_more_items: True
              new_latent_count: 20  三个参数
    """
    def get_all_min_position_id(self):
        opener = urt.build_opener()  # urllib创建开启url器
        # 设置头文件参数: User-agent, Cookie
        opener.addheaders = [('User-agent', self.user_agent)]
        opener.addheaders = [('Cookie', self.cookie)]
        count = 0
        flag = True
        while flag:
            page = opener.open(self.url, data=None, timeout=1000)
            content = page.read()  # 读取response文件
            # print("content:", content)
            # 将response文件转换成JSON格式，JSON转换成Python字典数据结构
            data = jsonlib.loads(content)
            # print("data:", data)
            # 获取字典数据结构内部的数据字段和值(key: value) new_latent_count":20
            min_position = int(data['min_position'])  # int
            mobile_id = str(min_position - 1)
            min_position = str(min_position)
            print("min_po:", min_position, ", mo_id:", mobile_id)
            # has_more_items = data['has_more_items']  # int
            new_latent_count = data['new_latent_count']  # boolean
            # print("next_cursor:", min_position)
            if not (new_latent_count > 0):
                flag = False
            else:
                # 形成新的URL，在获取JSON
                next_url = "https://twitter.com/i/profiles/show/poke/timeline/with_replies?" \
                      "include_available_features=1" \
                      "&include_entities=1&max_position="+min_position+"&reset_error_state=false"
                self.url = next_url
                # 直接一个个的写入文本文件,获取一个就写一个
                mobile_next_url = "https://mobile.twitter.com/i/rw/profile/timeline?" \
                                  "max_id="+mobile_id+"&screen_name=poke&type=tweets"
                self.input_text(mobile_next_url)
                count += 1
                print("count:", count, ", next_cursor:", min_position)
                print("next_url:", self.url)
                print("\n")

# ----------------------------------------------------------------------------------------------------------

    """
    单个写入文本的方法
    """
    def input_text(self, next_url):
        # 打开文件
        fo = open(self.filename, "r+", encoding='utf-8')
        # 在文件末尾写上一行
        fo.seek(0, 2)
        fo.write(next_url)
        fo.write('\n')
        fo.close()

# ----------------------------------------------------------------------------------------------------------


def main_operation():
    """Part1: 设置参数"""
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, " \
                 "like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    cookie = "guest_id=v1%3A148482531768369694; mobile_metrics_token=148482538426969560;" \
             " zrca=5; kdt=um9UDXk2qUARHElvAh5qyd7unesk6QvMLYPverbd;" \
             " remember_checked_on=1; lang=zh-cn; ct0=f9aa7d1ee2765fa36367a11e211fdd78;" \
             " dnt=1; _mobile_sess=BAh7ByIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsY" \
             "XNoSGFzaHsABjoKQHVzZWR7ADoQX2NzcmZfdG9rZW4iJTViMjY1NTAwMmQzYjc5MDk5ZTUyMjg2ZDRm" \
             "ODRlMzI1--d47c9fabb6613c0b8a0e6c8d54e31ae533dc631a; _ga=GA1.2.1762403604.1484825327;" \
             " _gat=1; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6" \
             "Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCP8u5blZAToMY3NyZl" \
             "9p%250AZCIlMzFiZWRlMDViZGNhYmY5YTNkOWEwZDk2NTJlNTQxOWU6B2lkIiVjMzc3%250AMmRmZjB" \
             "mNjhlMjJmZWY1YjRkMWFiOWYyZjhiODoJdXNlcmwrCQBQlIB0%252FF0L--4650ca63a9eca887a5a" \
             "c096ad250735fa2b5ca7e"
    url = "https://twitter.com/i/profiles/show/lizardbill/timeline/with_replies?include_" \
          "available_features=1&include_entities=1" \
          "&max_position=822992703063543808&reset_error_state=false"
    # 写入文件名
    filename = "poke_twitter.txt"
    """Part2: 循环获取"""
    var = ParseTimeFlowData(user_agent, cookie, url, filename)  # 创建类的对象
    var.get_all_min_position_id()


# ----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)
