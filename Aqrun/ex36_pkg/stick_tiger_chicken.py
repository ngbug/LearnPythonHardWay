# -- coding: utf-8 --
"""
游戏杠子老虎鸡

"""

from random import randrange
from utils import str_input

class StickTigerChiken(object):
    """ Game class """

    hands = {
        1: '杠子',
        2: '老虎',
        3: '鸡',
        4: '虫',
    }

    success_list = [(1, 2), (2, 3), (3, 4), (4, 1)];
    fail_list = [(2, 1), (3, 2), (4, 3), (1, 4)];

    def __init__(self):
        self.robot_hand = 0;
    
    def generateRobotHand(self):
        self.robot_hand = randrange(1, 4)

    def getUserHand(self, show_menu=True):
        if show_menu:
            print("""
            ================
                1. 杠子
                2. 老虎 
                3. 鸡
                4. 虫
                
                0 返回游戏大厅
            ================
            """)
        user_hand = str_input("出手吧 > ")

        try:
            user_hand = eval(user_hand)
        except Exception:
            user_hand = -1
        return user_hand

    def showResult(self, user_hand, robot_hand):
        """Show game result"""
        result_set = (user_hand, robot_hand)

        if result_set in self.success_list:
            template_string = """
            
            %s  =>  %s
            恭喜你！ 你赢了~~
            
            """
        elif result_set in self.fail_list:
            template_string = """
            
            %s  =>  %s
            唉呀！不好意思你输了。再接再励吧~！
            
            """
        else:
            template_string = """
            
            %s  =>  %s
            不成继续。。。
            
            """
            print(template_string % (self.hands[user_hand], self.hands[robot_hand]))
            return self.run()

        print(template_string % (self.hands[user_hand], self.hands[robot_hand]))
        str_input('点击任意键继续...')
        self.run()

    def run(self, show_menu=True):
        """Main loop"""
        self.generateRobotHand()
        
        user_hand = self.getUserHand(show_menu)

        if user_hand == 0:
            print("欢迎再来~~")
        elif user_hand >=1 and user_hand <=4:
            self.showResult(user_hand, self.robot_hand)
        else:
            print("你是逗B吗？请不要乱输入...")
            self.run()

def start():
    """start"""
    game = StickTigerChiken()
    game.run()

if __name__ == "__main__":
    start()









