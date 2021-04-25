import threading


def func():
    print(threading.current_thread())


if __name__ == '__main__':
    for _ in range(5):
        my_func = threading.Thread(target=func)
        my_func.start()
