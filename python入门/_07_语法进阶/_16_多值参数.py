def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)
    print("-------")


demo(1)
demo(1, 2, 3, 4, 5)
demo(1, 2, 3, 4, name="wang", age=18)
