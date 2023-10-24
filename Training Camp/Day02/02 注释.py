# 导入一个random模块获取随机数
import random
import datetime

# 获取1-100 随机数
print(round(random.random() * 100))

# 打印当前时间： 格式 年/月/日 时:分:秒
print(datetime.datetime.now().strftime("%Y/%m/%d %X"))

"""
这是一个多行
注释
注释
注释
"""
