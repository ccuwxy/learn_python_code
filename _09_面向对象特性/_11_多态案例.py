class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s game" % self.name)


class XiaoTiaoDog(Dog):
    def game(self):
        print("%s fly game" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s and %s game" % (self.name, dog.name))
        dog.game()

# wangcai = Dog("旺财")

wangcai = XiaoTiaoDog("飞天旺财")
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)
