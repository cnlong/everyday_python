import curses   #curses 库 ( ncurses ) 提供了控制字符屏幕的独立于终端的方法
from random import randrange, choice # generate and place new tile
from collections import defaultdict

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']   #WASDRQ的ASCII编码
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']    #动作
actions_dict = dict(zip(letter_codes, actions * 2))     #创建动作字典，键名为ascii编码，值为动作名称

def get_user_action(keyboard):      #用户输入处理，循环+阻塞，直到获得有效输入才返回
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]       #返回的为ascii码

def transpose(field):       #矩阵转置
    return [list(row) for row in zip(*field)]

def invert(field):      #矩阵逆转
    return [row[::-1] for row in field]

class GameField(object):    #棋盘类，创建棋盘
    def __init__(self, height=8, width=8, win=2048):    #最经典的4*4～2048模式
        self.height = height
        self.width = width
        self.win_value = win    #过关分数
        self.score = 0  #当前分数
        self.highscore = 0  #最高分
        self.reset()    #棋盘重置

    def reset(self):    #重置棋盘
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]   #全部清零
        self.spawn()
        self.spawn()    #随机对两个空位进行赋值

    def move(self, direction):
        def move_row_left(row): #向左移动一行
            def tighten(row): #把零散的非零单元挤到一起 squeese non-zero elements together
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row): #对临近元素进行合并
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]    #分数更新，我们当前仍然在棋盘类中
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row) #判断长度是否一致，不一致报错
                return new_row
            return tighten(merge(tighten(row))) #挤在一起--》合并--》再次挤在一起

        #通过对矩阵进行转置与逆转，可以直接从左移得到其余三个方向的移动操作
        moves = {}
        moves['Left']  = lambda field:                              \
                [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                              \
                invert(moves['Left'](invert(field)))
        moves['Up']    = lambda field:                              \
                transpose(moves['Left'](transpose(field)))
        moves['Down']  = lambda field:                              \
                transpose(moves['Right'](transpose(field)))

        # 这部分代码和上述代码结构一致
        # moves = {}
        # moves['Left'] = lambda field: [move_row_left(row) for row in field]
        # moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        # moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        # moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):   #是否获胜
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):  #是否游戏结束，即判断是否仍然有一个方向可以移动
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()
        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

    def spawn(self):    #随机生成一个2或者4
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        #choice方法返回一个列表，元组或者字符串的随机项，上面一行语句把所有非零的位置组成一个列表给出并随机选择一个
        self.field[i][j] = new_element  #随机选中的一个非零位置赋值为2 或者 4

    def move_is_possible(self, direction):
        def row_is_left_movable(row):   #能否向左移动
            def change(i): # true if there'll be change in i-th tile
                if row[i] == 0 and row[i + 1] != 0: # Move
                    return True
                if row[i] != 0 and row[i + 1] == row[i]: # Merge
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left']  = lambda field:                              \
                any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:                              \
                 check['Left'](invert(field))

        check['Up']    = lambda field:                              \
                check['Left'](transpose(field))

        check['Down']  = lambda field:                              \
                check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

def main(stdscr):       #主逻辑
    def init():
        #重置游戏棋盘
        game_field.reset()
        return 'Game'
    #4  not_game函数表示我们已经不再游戏中，胜利或者游戏结束
    def not_game(state):
        game_field.draw(stdscr)
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)  #defaultdict可以接受一个函数作为参数来初始化,默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'    #对应不同的行为转换到不同的状态
        return responses[action]

    def game():     #在游戏中并判断用户下一步动作所带来的影响，重新游戏，退出，成功移动，随后返回用户动作结束后的状态
        #画出当前棋盘状态
        game_field.draw(stdscr)
        #读取用户输入得到action
        action = get_user_action(stdscr)

        if action == 'Restart':     #用户选择重开
            return 'Init'
        if action == 'Exit':        #用户选择退出
            return 'Exit'
        if game_field.move(action): # move successful   成功移动
            if game_field.is_win():     #游戏胜利，返回win
                return 'Win'
            if game_field.is_gameover():        #游戏失败，返回gameover
                return 'Gameover'
        return 'Game'

    state_actions = {       #状态字典
            'Init': init,
            'Win': lambda: not_game('Win'), #胜利，则会跳出游戏状态，根据win来判断条件，我们跳转至not_game函数来观察一下返回值
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    curses.use_default_colors()

    # 设置终结状态最大数值为 32
    game_field = GameField(win=64)

    state = 'Init'      #初识态

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main) 