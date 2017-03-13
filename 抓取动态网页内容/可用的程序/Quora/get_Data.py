"""
Name: 循环获取瀑布流网址的id参数
Author: Jia_qiu Wang(王佳秋)
Data: Jan, 2017
function:
"""

import time
import urllib.request as urt
import jsonlib
from html.parser import HTMLParser


class ParseTimeFlowData:

    # 类的公有参数
    # list_all_next_cursor = []

    """构造函数"""
    def __init__(self, user_agent, cookie, url, filename, user_name):

        self.user_agent = user_agent
        self.cookie = cookie
        self.url = url
        self.filename = filename
        self.user_name = user_name

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
            print("content:", content)
            content = str(content)
            print("type-content:", type(content))
            # 将response文件转换成JSON格式，JSON转换成Python字典数据结构
            data = jsonlib.loads(content)
            print("data:", data)
            # 获取字典数据结构内部的数据字段和值(key: value) new_latent_count":20
            min_position = data['min_position']  # str
            items_html = data['items_html']
            # 获取本页面的所有微博ID，调用方法：
            self.get_all_status_ids(items_html)
            new_latent_count = data['new_latent_count']  # int
            # print("next_cursor:", min_position)
            if not (new_latent_count > 0):
                flag = False
            else:
                # 形成新的URL，在获取JSON
                next_url = "https://twitter.com/i/profiles/show/"+self.user_name+"/timeline/with_replies" \
                           "?include_available_features=1" \
                           "&include_entities=1&max_position="+min_position+"&reset_error_state=false"
                self.url = next_url
                count += 1  # 计数器+1
                print("count:", count, ", next_cursor:", min_position)
                print("next_url:", self.url)
                print("\n")

# ----------------------------------------------------------------------------------------------------------

    """
    获取本页面的所有微博ID，调用方法：
    """
    def get_all_status_ids(self, items_html):
        hp = MyHTMLParser()
        hp.feed(items_html)
        hp.close()
        print("links:", hp.links)
        print("size-links:", len(hp.links))
        # 把list中的所有URL(相对地址)转换成绝对地址
        for i in hp.links:
            str_absolute_URL = "https://twitter.com" + i
            print("str_absolute_URL:", str_absolute_URL)
            # 写入到文本文件中
            self.input_text(str_absolute_URL)


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
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36" \
                 " (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    cookie = "m-b=\"Xb0jVMw7nHR4ALk0Bu1nFQ\075\075\"; m-s=\"be36VoAlhhlQ7bjYB5sGlg\075\075\";" \
             " m-css_v=b6a9d4fb55602580; m-early_v=83471c69fad5a4ed; m-tz=-480; m-wf-loaded=q-icons-q_serif;" \
             " _ga=GA1.2.1160086400.1486206954"
    user_name = "marcgravell"
    initial_max_position = "490083330575323136"
    url = "https://tch823564.tch.quora.com/up/chan32-8888/updates?min_seq=4276119137&channel=main-w-dep300" \
          "4-428742902611017586&hash=9683997917737376104&callback=jsonp15a09e025f91dad7b36e8313"
    ""
    # 写入文件名
    filename = "post.txt"
    """Part2: 循环获取"""
    var = ParseTimeFlowData(user_agent, cookie, url, filename, user_name)  # 创建类的对象
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
