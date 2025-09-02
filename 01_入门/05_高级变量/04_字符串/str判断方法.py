# 1. 判断空白字符
space_str = "\t\n\r"
print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
# num_str = "1.1"
# num_str = "\u00b2" #unicode 键盘上无法直接输入的字符
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit()) # 如果字符串中只包含数字返回True，全角数字、(1)、\u00b2
print(num_str.isnumeric()) # 如果字符串中只包含数字返回True，全角数字，汉字数字