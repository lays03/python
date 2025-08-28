"""
while 条件(判断 计数器 是否达到 目标次数):
    条件满足，做的事情1
    条件满足，做的事情2
    条件满足，做的事情3

    处理条件(计数器+1)
"""

row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        col += 1
    print("")
    row += 1

