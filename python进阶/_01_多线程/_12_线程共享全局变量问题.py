import threading
import time

g_nums = 0


def sum_num1():
    global g_nums
    for i in range(1000000):
        g_nums += 1
    print("sum_num1:", g_nums)


def sum_num2():
    global g_nums
    for i in range(1000000):
        g_nums += 1
    print("sum_num2:", g_nums)


if __name__ == '__main__':
    sub_num1 = threading.Thread(target=sum_num1)
    sub_num2 = threading.Thread(target=sum_num2)

    sub_num1.start()
    sub_num2.start()
