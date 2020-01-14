"""
添加命令组
"""
import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    for x in range(count):
        print('Hello %s!' % name)


@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    click.echo('%s / %s' % pos)


cli.add_command(hello)
cli.add_command(findme)
if __name__ == '__main__':
    cli()