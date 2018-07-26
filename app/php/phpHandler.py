from app.helper import hostTemplateMaps, mapping, templateLoader, error, info
from app.configs import *

def _createVirtualHost(domain,content):
    """
    Create VirtualHost File
    :param content: Your Content That you want Write to File
    :return: True if File Created , False if Not Created
    """
    try:
        VirtualHostFileAddress = "{}{}{}".format(VIRTUAL_HOSTS_PATH,domain,EXTENSION)
        with open(VirtualHostFileAddress,'w') as file:
            file.write(content)
        info("VirtualHost Created On '{}'".format(VirtualHostFileAddress))
        return True
    except Exception as e:
        error('_createVirtualHost from phpHandler file', (e))

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
        error('__backup from phpHandler file', (e))

def _addToHosts(domain):
    """
    Add Your Domain in configs.HOSTS
    :param domain: Your Domain
    """
    try:
        __backup(HOSTS)
        data = mapping(templateLoader(HOST_TEMPLATE_NAME),hostTemplateMaps(
            domain=domain
        ))
        with open(HOSTS,'a') as file:
            file.write("{}\n".format(data))
        info("Added Domain On '{}'".format(HOSTS))
        return True
    except Exception as e:
        error('_addToHosts from phpHandler file', (e))