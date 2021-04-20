class Cat:

    def __init__(self, name):
        self.name = name

        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)


tom = Cat("Tom")
print(tom.name)

del tom

print("-"*50)
