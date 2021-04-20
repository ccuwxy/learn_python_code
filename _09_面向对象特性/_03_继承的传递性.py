class Animal:
    def eat(self):
        print("eat---")

    def drink(self):
        print("drink-")

    def run(self):
        print("run-")

    def sleep(self):
        print("sleep-")


class Dog(Animal):

    def bark(self):
        print("bark")


class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")


wangCai = Dog()
wangCai.eat()
wangCai.drink()
wangCai.run()
wangCai.sleep()
wangCai.bark()

xiaoTianQuan = XiaoTianQuan()
xiaoTianQuan.fly()
xiaoTianQuan.bark()
xiaoTianQuan.eat()
