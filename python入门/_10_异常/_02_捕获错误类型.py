try:
    num = int(input("请输入整数："))

    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("请输入正确的整数！")
