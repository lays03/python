# # 1. 定义一个整数变量记录年龄
# age = int(input("请输入年龄："))
#
# # 2. 判断是否满了18岁
# if age > 18:
#     # 3. 如果满了18岁
#     print("允许进入网吧！")
# elif age == 18:
#     print("刚满18岁！")
# else:
#     # 4. 如果未满18岁
#     print("未满18岁不允许进入网吧！")
from ssl import create_default_context

# age = int(input("请输入年龄："))
#
# if 0 <= age <= 120:
#     print("年龄符合条件")
# else:
#     print("年龄不符合条件")

# python_score = float(input("请输入python成绩："))
#
# c_score = float(input("请输入c成绩："))
#
# if python_score > 60 or c_score > 60:
#     print("成绩合格")
# else:
#     print("成绩不合格")


# # 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用not
# # 另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用not
# is_employee = False
#
# if not is_employee:
#     print("非本公司人员，请勿入内")
# else:
#     print("确认本公司人员，欢迎")

has_ticket = True
knife_length = 20

if has_ticket:
    print("持有火车票，请进入安检")
    if knife_length < 20:
        print("安检通过")
    else:
        print("刀的长度过长，不允许上车")
else:
    print("请先购票")