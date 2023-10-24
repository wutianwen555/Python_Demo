# (5) isdigit
# numStr = input("请输入一个数字：")  # "123"
#
# # 先判断numStr是否是一个数字字符串
# # print(numStr.isdigit())
#
# if numStr.isdigit():
#     # numStr是一个纯数字字符串
#     # 类型转换
#     num = int(numStr)  # "123" ==>  123
#     print(num * 2)
# else:
#     # numStr不是一个纯数字字符串
#     print("输入有误，请输入一个纯数字！")


# (6) strip：去除字符串两端的空格或换行符
user = input("请输入用户名：")
user = user.strip()
print(user, len(user))
