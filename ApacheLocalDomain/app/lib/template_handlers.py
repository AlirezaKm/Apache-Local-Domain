import os

from ApacheLocalDomain.app import configs
from ApacheLocalDomain.app.lib.log import error


def templateLoader(template):
    file = "{}/{}/{}".format(
        os.path.abspath("{}/../../..".format(__file__)),
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
        "{wsgi_script}": wsgiScript,
        "{email}": email,
        "{static_folder_name}": StaticFolderName,
        "{virtualenv_folder_name}": virtualenv,
    })

    out.update({"#{enable_static}": ''} if enable_static else {"{enable_static}": ''})
    out.update({"#{enable_http_2}": ''} if http2 else {"{enable_http_2}": ''})

    return out


def phpTemplateMaps(document_root, server_name, server_admin, http2):
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
        text = (text).replace('{}'.format(i), '{}'.format(dictionary[i]))
    return text
