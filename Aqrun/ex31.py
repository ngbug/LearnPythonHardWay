# -- coding: utf-8 --
"""
习题 31: 作出决定
"""

print("你现在在一个黑屋子，有两个门。你想走1号门还是2号门？")

door = raw_input("> ")

if door == "1":
    print("这有一个巨大的棕熊在吃奶酪蛋糕。你要怎么办？")
    print("1. 抢蛋糕。")
    print("2. 朝棕熊大叫。")

    bear = raw_input("> ")

    if bear == "1":
        print("一番挣扎棕熊把你整个脸都吃掉了。干得漂亮!")
    elif bear == "2":
        print("一番挣扎棕熊把你双腿都吃了。干得漂亮!")
    else:
        print("好吧, 现在按%s做或许会好点。棕熊跑远了。" % bear)
    
elif door == "2":
    print("门开了，脚下就是悬崖绝壁，放眼望去尸横遍野，凛冽的寒风夹杂着血腥味迎面扑来。")
    print("1. 你纵身跳下了悬崖")
    print("2. 你试着沿峭壁往东走。")
    print("3. 你大喊了几声救命，希望有人能听到。")

    insanity = raw_input("> ")

    if insanity == "1":
        print("刺骨的河水包围了你，用尽最后力气游上了岸，你得救了！")
    else:
        print("几分钟后，突然一个炮弹正中你的身后，你被炸得尸骨无存。。。")
else:
    print("噗嗵！你摔了一跤，死了！")