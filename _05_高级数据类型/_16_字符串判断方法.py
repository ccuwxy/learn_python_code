space_str = "     \t \r\n"

print(space_str.isspace())

# 判断字符串中是否只包含数字
# 1. 都不能判断小数
num_str = "\u00b2"
print(num_str.isdecimal())  # 全角数字
print(num_str.isdigit())    # 全角数字和Unicode数字
print(num_str.isnumeric())  # 全角数字、中文数字、unicode数字
