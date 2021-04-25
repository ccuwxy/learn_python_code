import multiprocessing


# 带有参数的函数传参
def dance(count):
    print(multiprocessing.current_process())
    for i in range(count):
        print("跳舞")


if __name__ == "__main__":
    # 创建子进程
    # Process：
    # target：指定执行的任务名（函数名）
    # args:
    # kwargs:
    # my_dance = multiprocessing.Process(target=dance, args=(5,))
    my_dance = multiprocessing.Process(target=dance, kwargs={"count": 2})

    my_dance.start()
