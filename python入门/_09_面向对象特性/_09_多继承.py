class A:

    def test(self):
        print("test 方法")


class B:

    def demo(self):
        print("demo 方法")


class C(A, B):
    """
    多继承可以让子类对象，同时拥有多个父类的属性和方法
    """
    pass


c = C()
c.test()
c.demo()
