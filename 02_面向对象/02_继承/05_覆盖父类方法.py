# 动物类
class Animal:
    def eat(self):
        print("吃--")

    def drink(self):
        print("喝--")

    def run(self):
        print("跑--")

    def sleep(self):
        print("睡--")


# 子类拥有父类的所有属性和方法
class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    def bark(self):
        print("叫得跟神一样...")

xtq = XiaoTianQuan()
xtq.bark()
