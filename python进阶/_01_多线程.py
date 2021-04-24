import time


def dance():
    for i in range(5):
        time.sleep(1)
        print("跳舞", i)


def sing():
    for i in range(5):
        time.sleep(1)
        print("唱歌", i)


if __name__ == '__main__':
    dance()
    sing()
