def test(num):
    print("test 中 %s 地址 %d" % (num, id(num)))

    result = "hello"

    print("result要返回的地址是 %s" % id(result))

    return result


a = 10

print("%d 地址 %d" % (a, id(a)))

test_result = test(a)

print("result返回的地址是 %s" % id(test_result))