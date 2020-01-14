from __future__ import unicode_literals
from prompt_toolkit import prompt
# 导入历史模块类，实现查找历史的功能
from prompt_toolkit.history import FileHistory
# 实现用户输入时候自动提示
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
# tab自动补全提示命令,旧版的WordCompleter不可用了
from prompt_toolkit.contrib.completers import SystemCompleter


SQLCompleter = SystemCompleter()


while True:
    user_input = prompt('>', history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=SQLCompleter, )
    print(user_input)