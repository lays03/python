import cards_tools

card_list = []

while True:
    print("*" * 30)
    print("欢迎使用【名片管理系统】 V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 30)
    action = input("请输入您想要的操作：")
    action_str = ['0', '1', '2', '3']

    if action == action_str[1]:
        card_dict = cards_tools.new_card() # 新建名片 返回新建的名片信息
        print(card_dict) #打印新建名片的信息
        card_list.append(card_dict) #将新建名片的信息添加到系统中
        print("添加成功 %s 的信息" % card_dict["name"])
    elif action == action_str[2]:
        cards_tools.print_card(card_list) #打印系统中所有名片的信息
    elif action == action_str[3]:
        search_name = input("请输入您想要查询名片的姓名：")
        res_dict = cards_tools.search_card(card_list, search_name) # 通过姓名查询名片
        if res_dict:
            print("-*-" * 30)
            print("查询成功，该人的详细信息为：", end="")
            print(res_dict)
            print("1. 修改名片信息")
            print("2. 删除名片信息")
            print("0. 取消后续操作")
            print("-*-" * 30)
            temp_action = int(input("请选择后续操作："))
            if temp_action == 1:
                res_dict = cards_tools.modify_card(res_dict) # 修改名片信息
                print("修改完成！")
                print("修改后的信息为：", end="")
                print(res_dict)
            elif temp_action == 2:
                # 通过名片信息确定在系统中的索引
                # 并根据索引删除名片信息
                card_list.pop(card_list.index(res_dict))
                print("删除成功！")
            else:
                break
        else:
            print("查询失败，系统里查无此人！")
    elif action == action_str[0]:
        print("欢迎下次使用，再见！")
        break
    else:
        print("输入失败，请重新输入！")
