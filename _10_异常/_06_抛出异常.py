def input_password():
    password = input("请输入密码：")

    if len(password) >= 8:
        return password

    ex = Exception("密码长度不够！")

    raise ex


try:

    print(input_password())
except Exception as re:
    print(re)
