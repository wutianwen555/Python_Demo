# 案例1
# chinese = 148
# math = 150
#
# # 第一次谈判:两科同时满分给予奖励
# print(chinese == 150 and math == 150)
# # 第二次谈判:两科只要有一科满分给予奖励
# print(chinese == 150 or math == 150)

# 案例2 范围判断  年龄： 20-35

# age = 23
# print(age > 20 and age < 35)
# print(20 < age < 35)


# 案例3 登录判断
# 可以访问用户
# user = "root"
# pwd = "123"
#
# username = input("请输入用户名：")
# password = input("请输入密码：")
#
# print(user == username and pwd == password)

# 案例4 条件嵌套

chinese = 148
math = 150
total = 640

# 总成绩大于700分或者语文和数学同时满分

print(total>700 or (chinese==150 and math==150))





















