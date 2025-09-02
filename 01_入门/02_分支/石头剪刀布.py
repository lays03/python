#导入随机工具包
import random

# 1. 从控制台输入要出的拳--石头（1） 剪刀（2） 布（3）
player = int(input("请输入您要出的拳 -- 石头（1） 剪刀（2） 布（3）"))

# 2. 电脑随机出拳--先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)

print("玩家出的拳是 %d - 电脑出的拳师 %d " % (player, computer))

# 3. 比较胜负
# 石头 胜 剪刀
# 剪刀 胜 布
# 布 胜 石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("恭喜您获胜，电脑弱爆了！")
elif player == computer:
    print("平局")
else:
    print("很遗憾，电脑获胜...")
