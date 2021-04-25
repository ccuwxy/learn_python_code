import threading
import time


def func():
    for i in range(5):
        time.sleep(0.2)
        print("func")


if __name__ == '__main__':
    my_func = threading.Thread(target=func, daemon=True)

    # my_func.setDaemon(True)
    my_func.start()

    time.sleep(0.5)
    print("over")
