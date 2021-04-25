import multiprocessing

def dance():
    print(multiprocessing.current_process())
    for i in range(5):
        print("跳舞")


if __name__ == "__main__":

    # 创建子进程
    # Process：
    # target：指定执行的任务名（函数名）
    # name:子进程起名
    my_dance = multiprocessing.Process(target=dance, name="老王")

    my_dance.start()