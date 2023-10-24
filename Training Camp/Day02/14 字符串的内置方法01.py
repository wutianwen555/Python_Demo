# 数据类型的内置方法： 数据类型对象.方法名(参数)

# 1  upper lower 方法
s1 = "Hello World"
s2 = "hello yuan"
num = 100
# print(type(s1))  # <class 'str'>

# s1Upper = s1.upper()
# print(s1Upper)  # HELLO WORLD
# print(s1)  # Hello World
print(s1.upper())
print(s2.upper())
# print(num.upper())
print(s1.lower())  # hello world
print(s2.lower())  # hello yuan

# 2 startswith  endswith 方法

s3 = " apple banana peach orange"
print("banana" in s3)
# 字符串是否以什么内容开头
print(s3.startswith("apple"))
print(s3.startswith(" apple"))
print(s3.startswith(" app"))
print(s3.startswith(" a"))
name = "张杰"
print(name.startswith("李"))
print(name.startswith("张"))
# 字符串是否以什么内容结尾
url1 = "https://www.baidu.com/aaa/bbb/ccc/a.png"
url2 = "https://www.baidu.com/aaa/bbb/ccc/b.jpg"
url3 = "https://www.baidu.com/aaa/bbb/ccc/c.mp3"
print(url1.endswith(".jpg"))
print(url2.endswith(".jpg"))
print(url3.endswith(".jpg"))





