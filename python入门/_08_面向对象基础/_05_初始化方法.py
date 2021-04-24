class Cat:

    def __init__(self):
        print("This is a init method!")
        self.name = "Tom"

    def eat(self):
        print("%s like to eat fish!" % self.name)


tom = Cat()

print(tom.name)

