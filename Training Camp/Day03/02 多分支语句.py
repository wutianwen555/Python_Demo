'''

if 表达式1:
    语句1
    语句2
    语句n
elif 表达式2 :
    语句3
    语句4
    语句n
elif 表达式3 :
    语句5
    语句6
    语句7
else:
    语句8
    语句9
    语句n

'''
height = float(input("请输入您的身高【米】："))
weight = float(input("请输入您的体重【公斤】："))

BMI = weight / height ** 2
print(BMI)

if BMI <= 18.5:
    print("偏瘦")
elif BMI < 24:
    print("正常")
elif BMI < 28:
    print("超重")
else:
    print("肥胖")
