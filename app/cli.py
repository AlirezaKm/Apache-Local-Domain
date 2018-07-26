import click
from app.php.cli import php
from app.wsgi.cli import wsgi

@click.group()
def cli():
    pass

cli.add_command(php)
cli.add_command(wsgi)