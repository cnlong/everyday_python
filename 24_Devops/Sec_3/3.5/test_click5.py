"""
linux的fc命令，以编辑器的方式打开上一条命令，可以编辑修改，保存退出自动运行
click也可以实现类似功能
"""
import click


# message = click.edit()
# print(message, end='')

@click.command()
@click.option('--count', type=click.IntRange(0, 20, clamp=True))
@click.option('--digit', type=click.IntRange(0, 10))
def repeat(count, digit):
    click.echo(str(digit) * count)


if __name__ == '__main__':
    repeat()

