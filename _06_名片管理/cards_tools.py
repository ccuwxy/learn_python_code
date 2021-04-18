# 记录所有名片字典
card_list = []


def show_menu():
    """
    显示菜单
    :return:
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """
    新增名片
    :return:
    """
    print("-" * 50)
    print("新增名片")

    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }

    card_list.append(card_dict)

    print(card_list)

    print("添加 %s 的名片成功" % name_str)


def show_all():
    """
    显示全部名片
    :return:
    """
    print("-" * 50)
    print("显示全部名片")

    if len(card_list) == 0:
        print("当前没有任何名片记录，请添加！")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print()
    print("-" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" %
              (card_dict["name"],
               card_dict["phone"],
               card_dict["qq"],
               card_dict["email"]))
    print("-" * 50)


def search_card():
    """
    搜索名片
    :return:
    """
    print("-" * 50)
    print("搜索名片")

    find_name = input("请输入要搜索的姓名：")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" %
                  (card_dict["name"],
                   card_dict["phone"],
                   card_dict["qq"],
                   card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("没有找到 %s ！！" % find_name)


def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict: 查找到的名片
    :return:
    """
    action_str = input("请选择要进行的操作："
                       "[1] 修改名片 [2] 删除名片  [0] 返回主菜单")
    if action_str == "1":
        modify_card(find_dict)
    elif action_str == "2":
        delete_card(find_dict)
    elif action_str == "0":
        return


def modify_card(find_dict):
    """
    修改查找到的名片
    :param find_dict: 查找到的名片
    :return:
    """
    find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
    find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
    find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
    find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
    """
    new_name = input("姓名：")
    if new_name != "":
        find_dict["name"] = new_name

    new_phone = input("电话：")
    if new_phone != "":
        find_dict["phone"] = new_phone

    new_qq = input("QQ：")
    if new_qq != "":
        find_dict["qq"] = new_qq

    new_email = input("邮箱：")
    if new_email != "":
        find_dict["email"] = new_email
    """
    print("修改名片成功！！")


def delete_card(find_dict):
    """
    删除查找到的名片
    :param find_dict:查找到的名片
    :return:
    """
    card_list.remove(find_dict)
    print("删除名片成功！！")


def input_card_info(dict_value, tip_msg):
    """
    输入名片信息
    :param dict_value:字典中原有的值
    :param tip_msg:输入的提示信息
    :return:如果输入了信息就返回输入的，没输入，返回原有值
    """
    result_str = input(tip_msg)
    if result_str == "":
        return dict_value
    else:
        return result_str

