name_list = ["zhangsan", "lisi", "wangwu"]

print(name_list[2])

# value 不存在 会报错
print(name_list.index("wangwu"))

name_list[1] = "李四"

name_list.append("wanger")
name_list.insert(2, "wangxiaoer")
name_list.extend(["孙悟空", "沙师弟"])

name_list.remove("wangwu")
print(name_list.pop())
name_list.clear()
print(name_list)

