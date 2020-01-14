import click
import codecs

@click.command()
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def encrypt(password):
    click.echo('Encrypting password to %s' % password)


# click 也提供了一种快捷的方式，通过使用 @click.password_option()
@click.command()
@click.password_option()
def input_password(password):
    click.echo('password: %s'% password)

if __name__ == '__main__':
    # encrypt()
    input_password()