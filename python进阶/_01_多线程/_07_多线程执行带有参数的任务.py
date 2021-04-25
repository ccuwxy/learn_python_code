import time
import threading


def dance(count):
    for i in range(count):
        print("dance", i)
        time.sleep(0.3)


if __name__ == '__main__':
    # my_dance = threading.Thread(target=dance, args=(5,))
    my_dance = threading.Thread(target=dance, kwargs={"count": 5})

    my_dance.start()
