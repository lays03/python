class Cat:
    """
    这是一个猫类
    """
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

tom = Cat()
tom.eat()
tom.drink()


lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

print(tom)
print(lazy_cat)
