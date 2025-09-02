# 字典是一个无序的数据集合，使用print函数输出字典时，通常
# 输出的顺序和定义的顺序是不一致的
xiaoming_dict = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}

# 1. 取值
print(xiaoming_dict["name"])

# 2. 增加/修改
# 如果Key不存在，会新增键值对
xiaoming_dict["wife"] = "小红"
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"

# 3. 删除
xiaoming_dict.pop("name")


print(xiaoming_dict)