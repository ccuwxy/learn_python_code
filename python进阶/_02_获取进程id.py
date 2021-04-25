import time
import multiprocessing
import os


def dance():
    print("子进程id：", os.getpid())
    print("父进程id：", os.getppid())


def sing():
    print("子进程id：", os.getpid())
    print("父进程id：", os.getppid())


if __name__ == '__main__':
    # 三个进程：一个主进程，二个子进程
    # 三个线程：一个进程一个线程
    print("主进程id：", os.getpid())
    # 创建子进程
    # Process：
    # target：指定执行的任务名（函数名）
    my_dance = multiprocessing.Process(target=dance)
    my_sing = multiprocessing.Process(target=sing)

    my_dance.start()
    my_sing.start()
