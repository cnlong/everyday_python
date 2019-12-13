# 定义用户行为列表，也就是这个游戏用户会产生的操作列表"上，下，左，右，游戏重置，退出"
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
# 游戏过程中键盘输入键"w a s d r q",将其转换为ascii值,便于后续捕捉键位操作
letter_codes = [ord(i) for i in 'WASDRQwasdrq']
# 将用户行为和键盘输入进行关联,通过zip函数进行组合,返回的是一个zip对象，通过dict转换成字典
actioncodes_dict = dict(zip(letter_codes, actions))


