# -- coding: utf-8 --
"""

游戏设计：
游戏大厅显示游戏列表：
石头剪刀布
杠子老虎鸡
"""

from rock_paper_scissors import start as rock_start
from stick_tiger_chicken import start as stick_start

def show_welcome_menu():
    """显示大厅欢迎列表"""
    print("""
    ==================================================
    #                                                #
                欢迎来到 *了扎咧* 游戏大厅          
                                                    
                   1. 石头剪刀布                    
                   2. 杠子老虎鸡
                
                   0. 退出游戏大厅
    #                                                #
    ==================================================
    """)


def main_hall():
    """游戏大厅 所有游戏列表"""
    next = -1

    while True:
        show_welcome_menu()

        #python3.0 raw_input rename to input
        next = input('你想玩什么游戏? > ')

        if next == '0':
            print("欢迎再来哦~~")
            break
        elif next == '1':
            rock_start()
        elif next == '2':
            stick_start()
        else:
            print("客官，不可以哦～～")

if __name__ == '__main__':
    main_hall()