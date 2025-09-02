class Person:
    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我叫%s ，我的体重是%.2fkg" % (self.name, self.weight)

    def run(self):
        #小明每次跑步会减肥 0.5kg
        self.weight -= 0.5
        print("%s跑完步了，体重下降了0.5kg，现在的体重是%.2fkg" % (self.name, self.weight))

    def eat(self):
        #小明每次吃东西体重增加1kg
        self.weight += 1
        print("%s吃完东西了，体重增加了1kg，现在的体重是%.2fkg" % (self.name, self.weight))

xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()

print(xiaoming)

# 小美爱跑步
xiaomei = Person("小美", 45)
xiaomei.run()
xiaomei.eat()

print(xiaomei)
print(xiaoming)