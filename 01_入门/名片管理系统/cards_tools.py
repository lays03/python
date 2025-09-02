def new_card():
    """
    新建名片
    :return: 返回card_list
    """
    name = input("请输入姓名：")
    tele = input("请输入电话号码：")
    qq = input("请输入QQ号码：")
    email = input("请输入邮箱：")
    card_dict = {"name": name, "tele": tele, "qq": qq, "email": email}
    return  card_dict

def print_card(card_list):
    """
    打印名片
    :return:
    """
    if len(card_list) == 0:
        print("系统为空！")
    else:
        for header in ["姓名", "电话号码", "QQ号码", "邮箱"]:
            print(header, end="\t\t")
        print("")

        print("=" * 50)
        for temp_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (temp_dict["name"],
                                            temp_dict["tele"],
                                            temp_dict["qq"],
                                            temp_dict["email"]))


def search_card(card_list, name):
    """
    查询名片
    :return:
    """
    for temp_dict in card_list: # 根据姓名查询名片
        if temp_dict["name"] == name:
            return temp_dict
    else:
        return False


def modify_card(res_dict):
    """
    修改名片
    :return:
    """
    action_str = ['0', '1', '2', '3', '4']
    while True:
        print("*-*" * 5)
        print("1. 修改name")
        print("2. 修改tele")
        print("3. 修改qq")
        print("4. 修改email")
        print("0. 退出修改")
        print("*-*" * 5)
        action = input("请选择需要修改的信息：")
        if action == action_str[1]:
            res_dict["name"] = input("请输入新的姓名：")
        elif action == action_str[2]:
            res_dict["tele"] = input("请输入新的电话号码：")
        elif action == action_str[3]:
            res_dict["qq"] = input("请输入新的QQ号码：")
        elif action == action_str[4]:
            res_dict["email"] = input("请输入新的邮箱：")
        elif action == action_str[0]:
            break
        else:
            print("输入失败，请重新输入！")
    return res_dict

def delete_card(card_list, res_dict):
    """
    删除名片
    :return:
    """
    card_list.remove(res_dict)