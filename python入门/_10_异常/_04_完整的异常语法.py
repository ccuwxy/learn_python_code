try:
    num = int(input("请输入整数："))

    result = 8 / num
    print(result)

except ValueError:
    print("请输入正确的整数！")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
    pass
finally:
    print("无论是否出现错误，都会执行")
    pass
