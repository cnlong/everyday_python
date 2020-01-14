import click


# commadn函数装饰，使得被装饰的函数成为命令行接口，也就是该函数能够从命令行中获取参数
@click.command()
# 增加命令行的选项
@click.option('--count', default=1, help='Number of greetings.')
# prompt选项，当没有直接指定name 这个参数或者默认值时，会交互模式提示输入
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    for x in range(count):
        # click.echo为了兼容python2和python3
        # click.echo('Hello %s!' % name)
        # python3可以直接使用print打印
        print('Hello %s!' % name)


if __name__ == '__main__':
    hello()