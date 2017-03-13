import urllib.request as urt
import jsonlib
import string

opener = urt.build_opener()  # urllib创建开启url器
# 设置头文件参数: User-agent, Cookie
opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                                    "AppleWebKit/537.36 (KHTML, "
                                    "like Gecko) Chrome/55.0.2883.87 Safari/537.36")]
opener.addheaders = [('Cookie', "m-b=\"Xb0jVMw7nHR4ALk0Bu1nFQ\075\075\"; m-s=\"be36VoAlhhlQ7bjYB5sGlg\075\075\";"
                                " m-css_v=b6a9d4fb55602580; m-early_v=83471c69fad5a4ed; m-tz=-480; m-wf-loaded=q-ico"
                                "ns-q_serif; _ga=GA1.2.1160086400.1486206954")]
page = opener.open("https://tch170417.tch.quora.com/up/chan32-8888/updates?min_seq=4274796479&channel=ma"
                   "in-w-dep3505-2944002901738499632&hash=11835125263837804143&callback=jsonp15"
                   "a09a3bcc6416ca304392bd", data=None,
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
print("new_latent_count:", data['new_latent_count'])
# print("items_html:", data['items_html'])




