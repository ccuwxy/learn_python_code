hello_str = "hello hello"

print(len(hello_str))

# 统计子字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("a"))  # 不报错

print(hello_str.index("llo"))
# print(hello_str.index("as"))  # 报错

