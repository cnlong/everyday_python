from random import choice, randrange


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

    # 定义随机元素生成的方法及其位置
    def spawn(self):
        # 随机生成4或者2，当随机数大于89时元素是4，当元素小于89的时候，元素是2
        new_element = 4 if randrange(100) > 89 else 2
        # 随机得到一个随机空白组的元组坐标，因为是要新生成一个元素在游戏中，所以必须出现在空白坐标中
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] ==0])
        self.field[i][j] = new_element


    # 定义重置方法
    def reset(self):
        # 更新最高分数
        if self.score > self.highscore:
            self.highscore = self.score
        # 初始化当前分数
        self.score = 0
        # 棋盘初始化，所以位置元素全部清零
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        # 生成新元素
        self.spawn()
        self.spawn()


