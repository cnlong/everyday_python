import click


@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    click.echo('%s / %s' % pos)


if __name__ == '__main__':
    findme() 