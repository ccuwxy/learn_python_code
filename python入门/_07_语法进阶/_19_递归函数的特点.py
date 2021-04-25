def sum_number(num):

    print(num)
    if num == 1:
        return
    # 自己调用自己
    sum_number(num - 1)


sum_number(3)
