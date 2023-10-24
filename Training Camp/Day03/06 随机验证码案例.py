import random
import string

s = ""
for i in range(5):
    # 随机生成一个字符
    # char = random.choice("0123456789abcdefghABCDEFG")
    print(string.ascii_lowercase)  # "abcdefghijklmnopqrstuvwxyz"
    print(string.ascii_uppercase)  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(string.digits)  # "0123456789"
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    # print("all_chars:", all_chars)
    random_char = random.choice(all_chars)
    print("random_char:", random_char)

    s += random_char

print(s)

# 补充

# s1 = "a"
# s2 = "b"
# print(s1+s2)

# s = ""
# for i in range(5):
#     # print(str(i)) # "0"
#     s += str(i)  # s = s+ str(i)
#
# print(s)
# # "01234"
