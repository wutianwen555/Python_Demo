pid = input("请输入你的身份证号：")
# 身份证号位数是否是18位
if len(pid) == 18:
    print("打印个人基本信息")
    # (1) 打印性别,身份证号倒数第二位如果是偶数，代表是女生，否则男生
    num = int(pid[16])  # "5"==>5
    if num % 2 == 0:
        print("性别：女性")
    else:
        print("性别：男性")
    # (2) 打印籍贯
    jiGuanCode = pid[:6]
    print("jiGuanCode", jiGuanCode)  # "100000" 120000 310000
    if jiGuanCode == "110000":
        print("籍贯：北京市")
    elif jiGuanCode == "120000":
        print("籍贯：天津市")
    elif jiGuanCode == "310000":
        print("籍贯：上海市")
    elif jiGuanCode == "500000":
        print("籍贯：重庆市")
    else:
        print("不是直辖市！")
else:
    print("输入位数有误！")
print("程序结束")
