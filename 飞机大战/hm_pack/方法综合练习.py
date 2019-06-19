class  Game:
    top_scrore=0
    def __init__(self,name):
        # self.top_score=0
        self.player_name=name
#
#
    @staticmethod
    def show_help():
        print("help")
#
#
#
    @classmethod
    def show_top_score(cls):
        print("最高分是%.2f"%cls.top_scrore)
#
#
    def start_game(self):
        print("%s game start"%self.player_name)

Game.show_help()


