import multiprocessing
import time
g_num = []


def write():
    global g_num
    """向全局变量num写数据"""
    for i in range(5):
        g_num.append(i)


def read():
    """读取全局变量的值"""
    global g_num
    print(g_num)


if __name__ == '__main__':
    # 创建子进程
    # Process：
    # target：指定执行的任务名（函数名）
    my_write = multiprocessing.Process(target=write)
    my_read = multiprocessing.Process(target=read)

    my_write.start()
    time.sleep(1)
    my_read.start()
    print(g_num)
