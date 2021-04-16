import random
# 108
player = int(input("请出拳 石头1 见到2 布3："))
computer = random.randint(1, 3)

print("玩家选择的是 %d - 电脑选择的是 %d" % (player,computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜")
elif player == computer:
    print("平局")
else:
    print("电脑胜")
