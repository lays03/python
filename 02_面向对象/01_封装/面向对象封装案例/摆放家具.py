class HouseItem:
    """
    家具类
    """
    def __init__(self, name, area):
        """

        :param name: 家具的名称
        :param area: 家具的占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)



class House:
    """
    房子类
    """
    def __init__(self, house_type, area):
        """

        :param house_type: 户型
        :param area: 总面积
        """
        self.house_type = house_type
        self.area = area

        #剩余面积
        self.free_area = area

        #家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        """
        添置家具
        :param item: 家具列表
        :return:
        """
        print("要添加 %s" % item)
        # 1. 添加家具面积
        if item.area <= self.free_area:
            # 2. 计算剩余面积
            self.free_area -= item.area
            # 3. 将家具的名称添加到列表中
            self.item_list.append(item.name)
            print("%s添加成功，剩余面积：%.2f" % (item.name, self.free_area))
        else:
            print("%s添加失败，剩余面积：%.2f" % (item.name, self.free_area))

# 1. 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

item_list = [bed, chest, table]

# 2. 创建房子对象
my_home = House("两室一厅", 60.00)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
