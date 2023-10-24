# 7 8 方法 split join
citys = "北京,哈尔滨,深圳,重庆,津"
ret = citys.split(",")
print(ret)  # ['北京', '哈尔滨', '深圳', '重庆']
print(len(ret))
# ['北京', '哈尔滨', '深圳', '重庆', '津']

# ret2 = ";".join(ret)
ret2 = "".join(ret)
print(ret2)  # "北京;哈尔滨;深圳;重庆;津"  "北京哈尔滨深圳重庆津"

# 9 10 find index： 查询子字符串的索引位置
s = "yuan rain alvin eric"
# ret = s.find("rain")
# ret = s.find("yua")
# ret = s.find("abc")  # 没有找到返回-1
# ret = s.index("rain")
# ret = s.index("yuan")
# ret = s.index("apple")
# print(ret)

# 11 count: 计数
names = "张三 李四 王五 张三 张三 赵六"
print(names.count("张三"))

# 12 replace：替换

info = "i am yuan; yuan is very nice,and yuan is very shuai!"
new_info = info.replace("yuan", "alvin")
print(info)
print(new_info)
