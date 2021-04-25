hello_str = "hello world"

print(hello_str.startswith("Hello"))

print(hello_str.endswith("world"))

# index同样可以查找指定字符串在大字符串的索引
# index 指定的字符串不存在会报错，find会返回-1
print(hello_str.find("llo"))

# replace会新生成一个字符串，不会修改原来的字符串
print(hello_str.replace("world", "python"))

print(hello_str)

