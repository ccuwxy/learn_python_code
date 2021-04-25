import threading
import time

g_nums = 0
mutex = threading.Lock()


def sum_num1():
    global g_nums

    mutex.acquire()
    for i in range(1000000):
        g_nums += 1
    mutex.release()
    print("sum_num1:", g_nums)


def sum_num2():
    global g_nums
    mutex.acquire()
    for i in range(1000000):
        g_nums += 1
    mutex.release()
    print("sum_num2:", g_nums)


if __name__ == '__main__':
    sub_num1 = threading.Thread(target=sum_num1)
    sub_num2 = threading.Thread(target=sum_num2)

    sub_num1.start()
    # 让主线程等待sub_num1执行完毕再继续进行
    # sub_num1.join()

    sub_num2.start()
