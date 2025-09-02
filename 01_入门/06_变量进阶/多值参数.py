# 有时候需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用多值参数
# Python中有两种多值参数：
# 参数名前加一个 * 可以接收元组
# 参数名前加两个 * 可以接收字典

# 一般在给多值参数命名时，习惯使用以下两个名字
    # *args 存放元组参数
    # **kwargs 存放字典参数

def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)

demo(1)
demo(1, 2, 3, 4, name = "小明", age = 20)