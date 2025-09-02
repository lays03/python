class Gun:
    """
    枪 类型，子弹数量
    """
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    # 装填子弹
    def add_bullet(self, count):
        self.bullet_count += count
        print("%s [剩余子弹：%d]装弹完成" % (self.model, self.bullet_count))

    # 发射子弹
    def shoot(self, count):
        if self.bullet_count >= count:
            self.bullet_count -= count
            print("%s [剩余子弹：%d]正在发射子弹" % (self.model, self.bullet_count))
        else:
            print("%s [剩余子弹：%d]子弹不足，正在装填子弹" % (self.model, self.bullet_count))
            self.add_bullet(count - self.bullet_count)



class Soldier:
    """
    士兵类 士兵姓名，士兵的枪
    """
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def __str__(self):
        return "%s的枪是%s" % (self.name, self.gun.model)

    # 士兵开火
    def fire(self, count):
        self.gun.shoot(count)
        print("%s拿着%s，正在开火" % (self.name, self.gun.model))



my_gun = Gun("AK47", 30)
my_soldier = Soldier("王宝强", my_gun)
my_soldier.fire(10)
my_soldier.fire(10)
my_soldier.fire(10)
my_soldier.fire(10)
print(my_soldier)