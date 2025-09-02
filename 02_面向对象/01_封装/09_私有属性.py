class Woman:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print("我的年龄是 %d" % self.__age)


woman = Woman("小美", 18)
# 私有属性和私有变量不能在类外访问
# print(woman.age)
# woman.__secret()