"""
Name: 循环获取瀑布流网址的id参数
Author: Jia_qiu Wang(王佳秋)
Data: Jan, 2017
function:
"""

import time
import re
from html.parser import HTMLParser


class ParseTimeFlowData:

    # 类的公有参数
    # list_all_next_cursor = []

    """构造函数"""
    def __init__(self, filename):

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
            # 读取网页文本
            fo = open("post.txt", "r+", encoding='utf-8')
            content = fo.read()
            print("str:", content)
            position = fo.tell()
            print("postion:", position, ", type:", type(content))
            fo.close()

            # 获取本页面的所有微博ID，调用方法：
            self.get_all_status_ids(content)


# ----------------------------------------------------------------------------------------------------------

    """
    获取本页面的所有微博ID，调用方法：
    """
    def get_all_status_ids(self, items_html):
        link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", items_html)
        print("links:", link_list)
        # 把list中的所有URL(相对地址)转换成绝对地址
        size = 0
        for i in link_list:
            print("i:", i)
            if i is "#":
                print("-------------------------------")
                continue
            if i.find("pages") is not -1:
                print("-------------------------------")
                continue
            if i.find("posts") is not -1:
                url = "https://www.facebook.com"+i
                size += 1
                print("type:", type(url), "URL:", url)
                # 写入到文本文件中
                self.input_text(url)
            if i.find("videos") is not -1:
                url = "https://www.facebook.com"+i
                size += 1
                print("type:", type(url), "URL:", url)
                # 写入到文本文件中
                self.input_text(url)
            if i.find("photo") is not -1:
                print("type:", type(i), "URL:", i)
                size += 1
                # 写入到文本文件中
                self.input_text(i)
            if i.find("story") is not -1:
                i = i.replace("amp;", "")
                url = "https://www.facebook.com"+i
                size += 1
                print("type:", type(url), "URL:", url)
                # 写入到文本文件中
                self.input_text(url)
            print("-------------------------------")
        print("size:", size)

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

#------------------------------------------------------------------------------------------------------------

    """
    HTMLParse解析HTML页面类-class
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

# ----------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------


def main_operation():
    """Part1: 设置参数"""

    # 写入文件名
    filename = "URLs.txt"
    """Part2: 循环获取"""
    var = ParseTimeFlowData(filename)  # 创建类的对象
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
