hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("He"))


# 2. 判断是否以指定字符串结束
print(hello_str.endswith("rld"))

# 3. 查找指定字符串
print(hello_str.find("ell"))


# 4. 替换字符串
# 注意：replace方法执行完成之后，会返回一个新的字符串
# 不会修改原有字符串的内容
print(hello_str.replace("llo", "LLO"))
print(hello_str)