import os

from ApacheLocalDomain.app import configs
from ApacheLocalDomain.app.lib.log import error
from validators import domain as domainValidator, email as emailValidator


def __validUrl(url):
    """
        Validate domain
    :param url: Get Url For Validate , Without "http", "https" and "www"
    :return: Valid URL , if Not , Return None
    """
    try:
        if not domainValidator(url):
            error('__validEmail from helper file', "Correct Domain: example.com\n without 'http', 'https' , 'www' =)")
        return url.replace("www.", '') if url.startswith("www.") else url
    except Exception as e:
        error('__validUrl from helper file', e)


def __validEmail(email):
    """
        Validate email
    :param email: get email to Validation
    :return: Valid Email , if not show ERROR and exit !
    """
    try:
        if not emailValidator(email):
            error('__validEmail from helper file', "Correct Email: ex@example.com")
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
        error('_checkWSGIEnabled from helper file', e)


def _checkHTTP2Enabled():
    try:
        enable_modules = os.listdir(configs.APACHE2_MODULES_PATH)
        for emodule in enable_modules:
            if emodule.__contains__("http2"):
                return True

        error('_checkHTTP2Enabled from helper file', "'http2' Module of Apache not found or Disable")
    except Exception as e:
        error('_checkHTTP2Enabled from helper file', e)


def __wsgiAddressValidation(
        documentRoot,
        wsgiScript,
        virtualenv,
        StaticFolderName,
        enable_static
):
    DOCROOT = os.path.abspath(documentRoot)
    # Validate DocumentRoot
    if ("/" not in documentRoot):
        if not os.path.exists(documentRoot):
            raise Exception("directory does not exist: {0}".format(documentRoot))
    # Validate wsgiScript
    if ("/" not in wsgiScript):
        if not os.path.exists(wsgiScript):
            raise Exception("directory does not exist: {0}".format(wsgiScript))
    # Validate Virtualenv Name
    if ("/" in virtualenv):
        raise Exception("directory does not valid: {0}".format(virtualenv))
    VIRTUALENV = os.path.join(DOCROOT, virtualenv)
    if not os.path.exists(VIRTUALENV):
        raise Exception("directory does not exist: {0}".format(VIRTUALENV))

    # validate Static Folder Name
    if enable_static:
        if ("/" in StaticFolderName):
            raise Exception("directory does not valid: {0}".format(StaticFolderName))
        STATIC_FOLDER_NAME = os.path.join(DOCROOT, StaticFolderName)
        if not os.path.exists(STATIC_FOLDER_NAME):
            raise Exception("directory does not exist: {0}".format(STATIC_FOLDER_NAME))


def __phpAddressValidation(
        documentRoot
):
    DOCROOT = os.path.abspath(documentRoot)
    # Validate DocumentRoot
    if ("/" not in documentRoot):
        if not os.path.exists(documentRoot):
            raise Exception("directory does not exist: {0}".format(documentRoot))
