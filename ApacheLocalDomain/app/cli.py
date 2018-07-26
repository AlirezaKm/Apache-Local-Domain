import click
from ApacheLocalDomain.app.php.cli import php
from ApacheLocalDomain.app.wsgi.cli import wsgi


@click.group()
def cli():
    pass


cli.add_command(php)
cli.add_command(wsgi)

if __name__ == "__main__":
    cli()
