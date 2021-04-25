num = 10


def demo1():
    global num
    num = 100
    print("demo1==> %d" % num)


def demo2():
    print("demo2==> %d" % num)


demo1()
demo2()
