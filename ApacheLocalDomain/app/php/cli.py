import click
from ApacheLocalDomain.app.helper import __validEmail, __validUrl, mapping, templateLoader, phpTemplateMaps, error, info, \
    _createVirtualHost, _addToHosts
from ApacheLocalDomain.app.configs import *

@click.command()
@click.option('-d','--domain','domain',
              required=True,
              prompt="Enter Domain Please",
              help="This Domain is Created (ServerName)  , example: example.com")
@click.option('-r','--root','documentRoot',
              required=True,
              prompt="Enter DocumentRoot PATH Please",
              help="DocumentRoot of Your website (DocumentRoot) , example: /srv/http/MyWebSite/")
@click.option('-e','--email','email',
              required=False,
              default=None,
              help="Your Email (ServerAdmin) , example: example@example.com")
@click.option('--http2',"http2",
              is_flag=True,
              default=False,
              help="Enable HTTP2 Protocol"
              )
def php(domain,documentRoot,email,http2):
    """
        Initialize PHP Template
    """
    try:
        # validation
        DOMAIN = __validUrl(domain)
        email = __validEmail(email if email else "admin@{}".format(DOMAIN))

        # get Result
        result = mapping(templateLoader(PHP_TEMPLATE_NAME), phpTemplateMaps(
            server_admin=email,
            document_root=documentRoot,
            server_name=DOMAIN,
            http2=http2
        ))

        # Try to Create VirtualHost File
        if not _createVirtualHost(DOMAIN,result) :
            error('php from cli file',"Cant Create VirtualHost File")

        # # Try add Domain to HOSTS file
        if not _addToHosts(DOMAIN):
            error('php from cli file', "Cant Add Domain to '{}' File".format(HOSTS))

        info('Now Reload Your Apache2 Service: `sudo systemctl reload apache2.service`')
    except Exception as e:
        error('php from cli file', e)