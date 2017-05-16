# -- coding: utf-8 --
"""

游戏设计：
游戏大厅显示游戏列表：
石头剪刀布
杠子 老虎 鸡
"""

from rock_paper_scissors import start as rock_start
from stick_tiger_chicken import start as stick_start

def show_welcome_menu():
    """显示大厅欢迎列表"""
    print("""
    ============================
    #                          #
    # 欢迎来到 *了扎咧* 游戏大厅   #
    #                          #
    #     1. 石头剪刀布          #
    #     2. 杠子 老虎 鸡        #
    #                          #
    ============================
    """)


def main_hall():
    "游戏大厅 所有游戏列表"
    show_welcome_menu()
    

    next = raw_input('你想玩什么游戏? > ')
    
    if next == '1':
        rock_start()
        pass
    elif next == '2':
        stick_start()
        pass
    else:
        print("客官，不可以哦～～")
