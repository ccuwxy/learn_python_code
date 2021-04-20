def sum_number(num):
    if num == 1:
        return 1

    return num + sum_number(num - 1)


result = sum_number(100)
print(result)
