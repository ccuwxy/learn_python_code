class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是%s 体重是%.2f" % (self.name, self.weight)

    def eat(self):
        self.weight += 1

    def run(self):
        self.weight -= 0.7


xiaoming = Person("小明", 75.0)
print(xiaoming)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)
