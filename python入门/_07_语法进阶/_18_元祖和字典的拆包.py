def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_num = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# 拆包语法，简化元组变量/字典变量的传递
demo(*gl_num, **gl_dict)
demo(1, 2, 3, name="xiaoming", age=8)
