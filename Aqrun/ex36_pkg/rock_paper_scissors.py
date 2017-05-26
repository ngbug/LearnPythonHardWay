# -- coding: utf-8 --
"""
游戏 剪刀石头布
"""

from random import randrange
from utils import str_input

class RockPaperScissors(object):
    """Game class"""

    hands = {
        1 : '石头',
        2 : '剪刀',
        3 : '布',
    }

    success_list = [(1, 2), (2, 3), (3, 1)]

    def __init__(self):
        # 保存电脑的手形
        self.robot_hand = 1

    def generateRobotHand(self):
        self.robot_hand = randrange(1, 4)

    def getUserHand(self):
        print("""
        ================
            1. 石头
            2. 剪刀 
            3. 布
            
            0 返回游戏大厅
        ================
        """)
        user_hand = str_input("出手吧 > ")
        try:
            user_hand = eval(user_hand)
        except Exception:
            user_hand = -1;
        return user_hand

    def showResult(self, user_hand, robot_hand):
        """Show game result"""
        result_set = (user_hand, robot_hand)

        if user_hand == robot_hand:
            template_string = """

            %s  =>  %s
            好尴尬啊~~ 出成一样的了。再来！！

            """
        elif result_set in self.success_list:
            template_string = """
            
            %s  =>  %s
            恭喜你！ 你赢了~~
            
            """
        else:
            template_string = """
            
            %s  =>  %s
            唉呀！不好意思你输了。再接再励吧~！
            
            """

        print(template_string % (self.hands[user_hand],
                   self.hands[robot_hand]))
        str_input('点击任意键继续...')
        self.run()

    def run(self):
        """Main loop"""
        self.generateRobotHand()
        user_hand = 0

        user_hand = self.getUserHand()

        if user_hand == 0:
            print("欢迎再来~~")
        elif user_hand >=1 and user_hand <=3:
            self.showResult(user_hand, self.robot_hand)
        else:
            print("你是逗B吗？请不要乱输入...")
            self.run()

def start():
    """start"""
    game = RockPaperScissors()
    game.run()

if __name__ == "__main__":
    start()

