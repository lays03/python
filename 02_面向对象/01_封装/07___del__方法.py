class Cat():
    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

# tom是一个全局变量
tom = Cat("Tom")

# del关键字可以删除一个对象
del tom
print("-" * 50)
