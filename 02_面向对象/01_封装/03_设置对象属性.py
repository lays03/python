class Cat:
    """
    这是一个猫类
    """

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")

# 创建猫对象
tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
