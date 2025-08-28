name = "小明"

student_no = 100

price = 8.5

weight = 4

money = price * weight

scale = 0.5

print("我的名字叫%s，请多多关照！我的学号是%06d" % (name, student_no))

print("苹果单价：%.01f元/斤，购买了%.01f斤，需要支付%.01f元" % (price, weight, money))

print("数据比例是%.02f%%" % (scale * 100))