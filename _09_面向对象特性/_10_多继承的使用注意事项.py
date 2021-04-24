class A:

    def test(self):
        print("A----- test 方法")

    def demo(self):
        print("A------ demo 方法")


class B:

    def test(self):
        print("B----- test 方法")

    def demo(self):
        print("B------ demo 方法")


class C(A, B):
    """
    多继承可以让子类对象，同时拥有多个父类的属性和方法
    """
    pass


c = C()

c.test()
c.demo()

# 确定C类的继承顺序
print(C.__mro__)
