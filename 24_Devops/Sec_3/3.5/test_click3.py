import click


@click.command()
# 设定参数只能取固定的几个值
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def digest(hash_type):
    click.echo(hash_type)


if __name__ == '__main__':
    digest()