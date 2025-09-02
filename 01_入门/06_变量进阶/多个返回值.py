def measure():
    temp = 39
    wetness = 100
    return temp, wetness

# 使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)