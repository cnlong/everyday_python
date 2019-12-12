class GameField(object):
    """定义棋盘初始化参数，包括棋盘的宽高、游戏胜利条件"""
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        # 当前的分数，初始值为0
        self.score = 0
        # 最高分，初始值为0
        self.highscore = 0
        # 棋盘重置
        self.reset()

