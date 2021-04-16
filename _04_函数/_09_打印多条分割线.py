def print_line(char, times):
    """
    打印单行分隔符
    :param char: 分割线使用的字符
    :param times: 分割字符重复的次数
    """
    print(char * times)


def print_lines(char, times, rows):
    """
    打印多行分割线
    :param char: 分割线使用的分隔字符
    :param times: 分割字符重复的次数
    :param rows:
    :return:
    """
    row = 0

    while row < rows:
        print_line(char, times)
        row += 1


print_lines("+", 50, 2)
