import click


# 这个函数设计到回调函数的固定写法
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('--version', '-v', is_flag=True, callback=print_version, expose_value=False,
              is_eager=True)
@click.option('--name', '-n', default='xiaoming', help='输入名称')
def hello(name):
    click.echo(name)


# 类似数据库的删库操作
# value值是传入的参数，也就是--yes
# ctx代表执行的流程，abort终止流程
#
def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@click.command()
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to drop the db?')
def dropdb():
    click.echo('Dropped all tables!')


# click.confirmation_option() 装饰器封装了以上功能
@click.command()
@click.confirmation_option(prompt='Are you sure you want to drop the db?')
def dropdb2():
    click.echo('Dropped all tables!')


if __name__ == '__main__':
    # hello()
    dropdb2()