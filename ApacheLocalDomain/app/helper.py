import os, logging

import click
from validators import domain as domainValidator , email as emailValidator
import ApacheLocalDomain.app.configs as configs
logging.basicConfig(format='[E] %(message)s', level=logging.ERROR)


def templateLoader(template):
    file = "{}/{}/{}".format(
        os.path.abspath("{}/../..".format(__file__)),
        configs.TAMPLATES_FOLDER,
        template
    )
    try:
        with open(file, 'r') as f:
            return f.read()
    except Exception as e:
        error('templateLoader from helper file', e)


def wsgiTemplateMaps(
    domain,
    documentRoot,
    wsgiScript,
    email,
    StaticFolderName,
    virtualenv,
    enable_static,
    http2,
):
    out = dict({
        "{domain}": domain,
        "{document_root}": documentRoot,
        "{wsgi_script}":wsgiScript,
        "{email}":email,
        "{static_folder_name}": StaticFolderName,
        "{virtualenv_folder_name}":virtualenv,
    })

    out.update({"#{enable_static}":''} if enable_static else {"{enable_static}":''})
    out.update({"#{enable_http_2}":''} if http2 else {"{enable_http_2}":''})

    return out

def phpTemplateMaps(document_root, server_name,server_admin,http2):
    out = dict({
        "{server_admin}": server_admin,
        "{document_root}": document_root,
        "{server_name}": server_name,
    })

    out.update({"#{enable_http_2}": ''} if http2 else {"{enable_http_2}": ''})

    return out

def hostTemplateMaps(domain):
    return dict({
        "{domain}": domain
    })

def mapping(text, dictionary):
    for i in dictionary:
        text = (text).replace('{}'.format(i),'{}'.format(dictionary[i]))
    return text

def __validUrl(url):
    """
        Validate domain
    :param url: Get Url For Validate , Without "http", "https" and "www"
    :return: Valid URL , if Not , Return None
    """
    try:
        if not domainValidator(url) :
            error('__validEmail from helper file',"Correct Domain: example.com\n without 'http', 'https' , 'www' =)")
        return url.replace("www.",'') if url.startswith("www.") else url
    except Exception as e:
        error('__validUrl from helper file', e)

def __validEmail(email):
    """
        Validate email
    :param email: get email to Validation
    :return: Valid Email , if not show ERROR and exit !
    """
    try:
        if not emailValidator(email) :
            error('__validEmail from helper file',"Correct Email: ex@example.com")
        return email
    except Exception as e:
        error('__validEmail from helper file', e)

def _checkWSGIEnabled():

    try:
        enable_modules = os.listdir(configs.APACHE2_MODULES_PATH)
        for emodule in enable_modules:
            if emodule.__contains__("wsgi"):
                return True

        error('_checkWSGIEnabled from helper file', "'mode_wsgi' Module of Apache not found or Disable")
    except Exception as e:
        error('_checkWSGIEnabled from helper file',e)

def _createVirtualHost(domain,content):
    """
    Create VirtualHost File
    :param content: Your Content That you want Write to File
    :return: True if File Created , False if Not Created
    """
    try:
        VirtualHostFileAddress = "{}{}{}".format(configs.VIRTUAL_HOSTS_AVAILABLE_PATH, domain, configs.EXTENSION)
        with open(VirtualHostFileAddress,'w') as file:
            file.write(content)
        info("VirtualHost Created On '{}'".format(VirtualHostFileAddress))
        _setLinkTo(VirtualHostFileAddress)
        return True
    except Exception as e:
        error('_createVirtualHost from helper file', (e))

def __backup(File):
    """
    Backup From Your File
    :param File: Your File
    """
    from time import strftime, gmtime
    try:
        with open(File,'r') as file:
            data = file.read()
        with open("{}.localadmin_{}.bkp".format(File,strftime("%Y-%m-%d_%H:%M:%S", gmtime())),'w') as file:
            file.write(data)
    except Exception as e:
        error('__backup from helper file', (e))

def _addToHosts(domain):
    """
    Add Your Domain in configs.HOSTS
    :param domain: Your Domain
    """
    try:
        __backup(configs.HOSTS)
        data = mapping(templateLoader(configs.HOST_TEMPLATE_NAME), hostTemplateMaps(
            domain=domain
        ))
        with open(configs.HOSTS, 'a') as file:
            file.write("{}\n".format(data))
        info("Added Domain On '{}'".format(configs.HOSTS))
        return True
    except Exception as e:
        error('_addToHosts from helper file', (e))


def _setLinkTo(thisFile):
    import os
    try:
        link = thisFile.replace(configs.VIRTUAL_HOSTS_AVAILABLE_PATH, configs.VIRTUAL_HOSTS_ENABLED_PATH)
        os.link(thisFile, link)
        info('Linked file "{}" to "{}"'.format(thisFile, link))
    except Exception as e:
        error('_setLinkTo from helper file', e)

def error(From, msg , DEBUG = configs.DEBUG):
    if DEBUG:
        logging.error("EXCEPTION [{}] - {}".format(From,msg))
    else:
        logging.error("{}".format(msg))
    exit(-1)

def info(msg):
    print("[*] {}".format(msg))

class RequiredIF(click.Option):
    def __init__(self, *args, **kwargs):
        self.required_if = kwargs.pop('required_if')
        assert self.required_if, "'required_if' parameter required"
        kwargs['help'] = (kwargs.get('help', '') +
            ' {} [required with {}]'.format(self.help if hasattr(self,'help') else '',self.required_if)
        ).strip()
        super(RequiredIF, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        we_are_present = self.name in opts
        other_present = self.required_if in opts

        if other_present:
            if not we_are_present:
                raise click.UsageError(
                    "Illegal usage: `%s` requires for `%s`" % (
                        self.name, self.required_if))
            else:
                self.prompt = None
        return super(RequiredIF, self).handle_parse_result(
            ctx, opts, args)