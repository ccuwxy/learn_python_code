import threading
import time

g_nums = []


def write():
    global g_nums

    for i in range(5):
        g_nums.append(i)


def read():
    global g_nums
    print(g_nums)


if __name__ == '__main__':
    my_write = threading.Thread(target=write)
    my_read = threading.Thread(target=read)

    my_write.start()
    time.sleep(1)
    my_read.start()
