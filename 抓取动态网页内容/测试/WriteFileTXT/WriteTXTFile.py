"""
将字符串写入文本文件
"""

# 打开文件
fo = open("runoob.txt", "r+", encoding='utf-8')
print("文件名：", fo.name)

str = "a345345发光时代ng23423你好山东昂--+！@#￥%……&*"
# 在文件的末尾写入一行
"""
seek() 方法语法如下：
fileObject.seek(offset[, whence])
参数
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
"""
fo.seek(0, 2)
line = fo.write(str)
fo.write('\n')

# # 读取文件所有内容
# fo.seek(0, 0)
# for index in range(6):
#     line = next(fo)
#     print("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()

































