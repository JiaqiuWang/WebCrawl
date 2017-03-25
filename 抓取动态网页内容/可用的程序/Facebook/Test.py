var_test = "/IsraeliAirForce.EN/photos/a.247957101913936.56748.234494436593536/1426177347425233/?type=3"

if var_test.find("photos/a.") is not -1:
    print("type:", var_test)
    # 写入到文本文件中
if var_test.find("photo") is not -1:
    print("type:", var_test)
    # 写入到文本文件中
# if i.find("photos/a") is not -1:
#     url = "https://www.facebook.com" + i
#     size += 1
#     print("type:", type(url), "URL:", url)
#     # 写入到文本文件中
#     self.input_text(url)

