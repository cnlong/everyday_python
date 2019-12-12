"""
状态机：处理游戏主逻辑的技术。（有限状态机），游戏实际上是多个状态之间的转换，通过转换函数，转变到下一个状态
2048游戏状态中，可以拆解为几个状态：
1.初始化：init
2.游戏循环中状态:game
3.胜利状态：win
4.结束状态：gameover
5.退出状态
状态机之间通过函数不断转换，直至Exit状态退出游戏。
"""
from collections import defaultdict


# init函数用来初始化游戏
def init():
    """初始化游戏棋盘"""
    # 初始化完成返回游戏对象
    return 'Game'


# 定义游戏结束时的状态函数,游戏结束状态提供"重置"和"退出"两种功能
def not_game(state):
    # defaultdict 在取不存在的Key，会返回一个默认值，且默认值是函数的返回值，所以定义的时候传入了一个函数
    responses = defaultdict(lambda : state)
    # 字典中新建两个键值对
    responses['Restart'], responses['Exit'] = 'Init', 'Exit'
    return responses[action]


# 定义游戏进行时的状态，只有不重置退出没有胜利结束的情况下，一直处于游戏状态
def game():
    """读取用户输入得到action，画出当前棋盘状态
        根据用户输入移动棋盘，然后判断游戏是否结束，结束返回结束状态，未结束则返回游戏
    """
    if action == "Restart":
        return 'Init'
    if action == "Exit":
        return 'Exit'
    if win :
        return 'Win'
    if defeat:
        return 'Gameover'
    return 'Game'

# 状态机循环，将状态及其对应函数定义成字典
state_actions = {
    'Init': init,
    'Win': lambda : not_game('Win'),
    'Gameover': lambda : not_game('Gameover')
    'Game': game
}

# 初始状态
state = 'Init'

# 状态机开始循环
while state != 'Exit':
    state = state_actions[state]()
