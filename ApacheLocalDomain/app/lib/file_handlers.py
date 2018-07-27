import os

from ApacheLocalDomain.app import configs
from ApacheLocalDomain.app.lib.log import info, error
from ApacheLocalDomain.app.lib.template_handlers import mapping, templateLoader, hostTemplateMaps


def _createVirtualHost(domain, content):
    """
    Create VirtualHost File
    :param content: Your Content That you want Write to File
    :return: True if File Created , False if Not Created
    """
    try:
        PATH = os.path.join(configs.VIRTUAL_HOSTS_AVAILABLE_PATH, domain)
        VirtualHostFileAddress = "{}{}".format(PATH, configs.EXTENSION)
        with open(VirtualHostFileAddress, 'w') as file:
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
        with open(File, 'r') as file:
            data = file.read()
        with open("{}.localadmin_{}.bkp".format(File, strftime("%Y-%m-%d_%H:%M:%S", gmtime())), 'w') as file:
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
