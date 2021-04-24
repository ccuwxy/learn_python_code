def demo1():
    return int(input("输入一个整数："))


def demo2():
    return demo1()


try:
    print(demo2())
except Exception as r:
    print(r)