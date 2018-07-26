import click

from ApacheLocalDomain.app.configs import WSGI_TEMPLATE_NAME, HOSTS
from ApacheLocalDomain.app.helper import _checkWSGIEnabled, RequiredIF, mapping, templateLoader, wsgiTemplateMaps, __validUrl, \
    __validEmail, error, info, _createVirtualHost, _addToHosts


@click.command()
@click.option('-d','--domain','domain',
              required=True,
              prompt="Enter Domain Please",
              help="This Domain is Created (ServerName)  , example: example.com")
@click.option('-r','--root','documentRoot',
              required=True,
              prompt="Enter DocumentRoot PATH Please",
              help="DocumentRoot of Your website (DocumentRoot) , example: /srv/http/MyWebSite/")
@click.option('-w','--wsgiscript','wsgiScript',
              required=True,
              prompt="Enter WSGIScriptAlias file Please",
              help="WSGIScriptAlias of Your website (WSGIScriptAlias) , example: /srv/http/MyWebSite/wsgi.py")
@click.option('-v','--virtualenv-folder-name','virtualenv',
              default=".venv",
              required=True,
              prompt="Enter virtualenv folder name",
              help="Virtualenv Folder name in Project PATH (default: .venv)"
              )
@click.option('-e','--email','email',
              required=False,
              default=None,
              help="Your Email (ServerAdmin) , example: example@example.com")
@click.option('--http2',"http2",
              is_flag=True,
              default=False,
              help="Enable HTTP2 Protocol"
              )
@click.option('--enable-static',"enable_static",
              is_flag=True,
              help="Enable using static files"
              )
@click.option('-s','--static-folder-name','StaticFolderName',
              default='static',
              cls=RequiredIF,
              required_if='enable_static',
              help="static folder name in Project PATH (default: static)"
              )
def wsgi(
        domain,
        documentRoot,
        wsgiScript,
        email,
        virtualenv,
        StaticFolderName,
        enable_static,
        http2,
):
    """
        Initialize WSGI Template
    """
    try:
        # Check Enable WSGI or NOT
        _checkWSGIEnabled()

        # validation
        DOMAIN = __validUrl(domain)
        email = __validEmail(email if email else "admin@{}".format(DOMAIN))

        # Load and Mapping
        result = mapping(templateLoader(WSGI_TEMPLATE_NAME),wsgiTemplateMaps(
            domain,
            documentRoot,
            wsgiScript,
            email,
            StaticFolderName,
            virtualenv,
            enable_static,
            http2,
        ))

        # Try to Create VirtualHost File
        if not _createVirtualHost(DOMAIN,result) :
            error('wsgi from cli file',"Cant Create VirtualHost File")

        # # Try add Domain to HOSTS file
        if not _addToHosts(DOMAIN):
            error('wsgi from cli file', "Cant Add Domain to '{}' File".format(HOSTS))

        info('Now Reload Your Apache2 Service: `sudo systemctl reload apache2.service`')
    except Exception as e:
        error('wsgi from cli file', e)


