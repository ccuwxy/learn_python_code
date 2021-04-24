# 全局变量、函数、类
def say_hello():
    print("hello")


if __name__ == "__main__":
    # 永远都是__main__
    print(__name__)
    # 文件被导入时，能够直接执行的代码不需要被执行！
    print("小明")
    say_hello()
