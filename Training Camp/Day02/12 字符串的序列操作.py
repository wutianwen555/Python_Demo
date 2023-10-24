s = "hello yuan"

# （1）索引操作： 字符串[索引]   查询字符
print(s[6])
print(s[0])
print(s[9])
print(s[-1])
print(s[-2])

# （2）切片操作： 字符串[开始索引:结束索引:step=1]  顾头不顾尾
print(s[0:5])
print(s[6:9])
print(s[6:-1])
print(s[6:])  # 缺省，取到最后一个值
print(s[:5])  # 缺省，从0开始取
print(s[-10:-5])  # 缺省，从0开始取
print(s[-4:])  # 缺省，从0开始取
print("s[-5:-10]:::", s[-5:-10])
print("s[5:0]:::", s[5:0:1])
print(s[0:5:3])
print("s[0:5:-1]:::", s[0:5:-1])
print("s[0:5:-1]:::", s[6:0:-1])
print("s[:]", s[:])
print("s[::-1]", s[::-1])

# (3) 拼接 +

s1 = "hello "
s2 = " yuan"
print(1 + 2)
print(s1 + s2)

name = "yuan"
age = "18"
s3 = f"我的姓名:{name}  我的年龄：{age}!"
print(s3)

print("我的姓名:" + name + "  我的年龄：" + age + "！")
# print("*******************************************")
print("*" * 100)


# （4）针对容器类型： 计算字符串对象的长度：元素的个数 解释器内置函数 len
s4 = "hello world"
print(len(s4))
s5 = "i am 苑"
print(len(s5))

# (5) 针对容器类型：in 判断  判断某个成员是否存在
s6 = "yuan rains eric alvin"
print("rain" in s6)
print("rains" in s6)
print("ra" in s6)
print("s e" in s6)
print("erc" in s6)







