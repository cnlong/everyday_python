actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(i) for i in 'WASDRQwasdrq']
actioncodes_dict = dict(zip(letter_codes, actions))

# 获取用户键盘输入,阻塞+循环
def get_user_action(keyboard):
    char = "N"
    while char not in actioncodes_dict:
        # 返回按下键位的ascii值
        char = keyboard.getch()
    # 返回输入键位对应的行为
    return actioncodes_dict[char]