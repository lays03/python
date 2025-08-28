info_tuple = ("zhangsan", 18, 1.75)

# 1. 取值和取索引
print(info_tuple[0])

print(info_tuple.index(1.75))

# 2. 统计计数
print(info_tuple.count(18))

# 3. 循环遍历
for my_info in info_tuple:
    print(my_info, end=" ")
print("")

# 格式化字符串后面的()本质上就是元组
info = ("张三", 18)
print("%s 的年龄是 %d" % info)

# 列表和元组之间可以互相转换
name_list = ["张三", "李四", "王五"]

name_tuple = tuple(name_list)

print(type(name_tuple))

