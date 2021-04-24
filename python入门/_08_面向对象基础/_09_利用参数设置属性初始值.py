class Cat:

    def __init__(self, name):
        print("This is a init method!")
        self.name = name

    def eat(self):
        print("%s like to eat fish!" % self.name)


tom = Cat("Tom")
print(tom.name)

lazy_cat = Cat("Lazy")
lazy_cat.eat()
