import time
import multiprocessing


def dance():
    for i in range(5):
        time.sleep(1)
        print("跳舞", i)


def sing():
    for i in range(5):
        time.sleep(1)
        print("唱歌", i)


if __name__ == '__main__':
    # 三个进程：一个主进程，二个子进程
    # 三个线程：一个进程一个线程

    # 创建子进程
    # Process：
    # target：指定执行的任务名（函数名）
    my_dance = multiprocessing.Process(target=dance)
    my_sing = multiprocessing.Process(target=sing)

    my_dance.start()
    my_sing.start()
