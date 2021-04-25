import threading
import time

g_nums = 0
mutex = threading.Lock()


def sum_num1():
    mutex.acquire()

    if g_nums == 1:
        return
    mutex.release()


def sum_num2():
    mutex.acquire()
    print("sum_num2:", g_nums)
    mutex.release()


if __name__ == '__main__':
    sub_num1 = threading.Thread(target=sum_num1)
    sub_num2 = threading.Thread(target=sum_num2)

    sub_num1.start()
    # 让主线程等待sub_num1执行完毕再继续进行
    # sub_num1.join()

    sub_num2.start()
