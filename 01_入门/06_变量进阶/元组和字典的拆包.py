# 在开发时，需要将元组或字典变量直接传递到函数内部时，就需要 拆包

def demo(*args, **kwargs):
    print(args)
    print(kwargs)

gl_nums = (1, 2, 3)
gl_dict = {"name" : "小明", "age" : 20}
print(gl_nums)
print(gl_dict)