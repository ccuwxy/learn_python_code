students = [
    {"name": "阿土"},
    {"name": "小美"}
]
find_name = "张三"
for stu_dict in students:
    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("find ok %s" % find_name)
        break
else:
    print("%s not in stu_dict" % find_name)
print("over")
