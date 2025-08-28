num_str = "0123456789"

# 1. 截取从2~5的字符串
print(num_str[2:6])

# 2. 从开始位置，每隔一个字符截取字符串
print(num_str[::2])

# 3. 从索引1开始每隔一个字符截取字符串
print(num_str[1::2])

# 4. 从2~末尾-1的字符串
print(num_str[2:-1])

# 5. 截取末尾两个字符
print(num_str[-2:])

# 6. 字符串逆序
temp_str = num_str[-1::-1]
print(temp_str)
print(num_str[-1::-1])