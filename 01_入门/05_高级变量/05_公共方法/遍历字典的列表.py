card_list = [{"name": "小明",
              "age": 18,
              "tele": "12345"},
             {"name": "小红",
              "age": 17,
              "tele": "999"}]

fine_name = "张三"

for card_dict in card_list:

    print(card_dict)

    if card_dict["name"] == fine_name:
        print("找到了 %s" % fine_name)

        # 如果找到，直接退出循环，不再遍历后续元素
        break
# 如果把for循环所有的遍历执行完而不是通过break退出的循环，
# 就会执行else下的代码块
else:
    print("抱歉没有找到 %s" % fine_name)

print("循环结束")