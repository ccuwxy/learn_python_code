class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息")

    @classmethod
    def show_top_score(cls):
        print("The top score is %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏了。。。" % self.player_name)


Game.show_help()
Game.show_top_score()
my_Game = Game("小明")
my_Game.start_game()
