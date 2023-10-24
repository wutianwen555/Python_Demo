# break:退出整个循环
# continue:退出当次循环

# for i in range(1, 11):
#
#     if i == 6:
#         break
#     print(i)
#
# print("process end")

# (1) 打印半径为1m-100m的圆的面积
# (2) 半径为1m-100m范围内找到第一个面积大于1000的半径值

for r in range(1, 101):
    # print(r)
    # 计算圆的面积：pai * r**2
    area = 3.1415926 * r ** 2

    if area > 1000:
        print(f"半径为{r}的圆的面积：{area}")
        break
