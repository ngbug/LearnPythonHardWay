# -- coding: utf-8 --
"""
习题 36: 设计和调试


游戏设计：
游戏大厅显示游戏列表：
石头剪刀布
杠子 老虎 鸡

"""

def show_welcome_menu():
    """显示大厅欢迎列表"""
    print("""
    ============================
    |
    | 欢迎来到 *了扎咧* 游戏大厅
    |     
    |     1. 石头剪刀布
    |     2. 杠子 老虎 鸡
    |
    ============================
    """)


def main_hall():
    "游戏大厅 所有游戏列表"
    show_welcome_menu()
    

    next = raw_input('你想玩什么游戏? > ')
    
    if next == '1':
        rock_paper_scissors()
    elif next == '2':
        stick_tiger_chicken()
    else:
        print("客官，不可以哦～～")

def rock_paper_scissors():
    "游戏剪刀石头布"
    pass

def stick_tiger_chicken():
    "游戏杠子老虎鸡"
    pass

