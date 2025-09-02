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
        # 1. 针对子类特有的需求，编写代码
        print("神一样的叫唤...")

        # 2. 使用super()，调用原本在父类中封装的方法
        # super().bark()
        Dog.bark(self)
        # 3. 增加其他子类的代码
        print("$^@*#&(@R")

xtq = XiaoTianQuan()
xtq.bark()

