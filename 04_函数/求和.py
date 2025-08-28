from idlelib.pyshell import restart_line


def sum_2_num(num1, num2):
    """两数求和"""

    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))
    return result

a = sum_2_num(10, 20)

print(a)