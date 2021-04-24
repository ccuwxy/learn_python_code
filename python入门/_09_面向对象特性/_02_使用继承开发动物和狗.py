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


wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()