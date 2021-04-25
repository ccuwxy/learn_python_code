import time
import threading

def dance():
    for i in range(5):
        print("dance", i)
        time.sleep(1)


def sing():
    for i in range(5):
        print("sing", i)
        time.sleep(1)


if __name__ == '__main__':
    my_dance = threading.Thread(target=dance)
    my_sing = threading.Thread(target=sing)

    my_dance.start()
    my_sing.start()
