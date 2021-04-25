import multiprocessing
import time


def func():
    for i in range(5):
        time.sleep(0.2)
        print("func")


if __name__ == '__main__':
    # 主进程会等待子进程结束，再结束
    my_func = multiprocessing.Process(target=func)  # 主进程创建了子进程
    # 方式一：设置主进程
    # my_func.daemon = True  # 必须在start之前设置

    my_func.start()  # 主进程开启了子进程

    time.sleep(0.5)
    # 方式二：手动设置
    my_func.terminate()
    print("主进程：over")
    exit()

