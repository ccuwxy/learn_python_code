class Cat:

    def __init__(self, name):
        self.name = name

        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)

    def __str__(self):
        return "I am %s" % self.name


tom = Cat("Tom")
print(tom)
