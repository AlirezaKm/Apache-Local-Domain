import os, logging
from validators import domain as domainValidator , email as emailValidator
import app.configs as configs
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

def phpTemplateMaps(document_root, server_name,server_admin):
    try:
        if (server_name is None) or (document_root is None):
            error('phpTemplateMaps from helper file', 'DocumentRoot or ServerName is Empty!')
        return {
            "{server_admin}": server_admin,
            "{document_root}": document_root,
            "{server_name}": server_name,
        }
    except Exception as e:
        error('phpTemplateMaps from helper file', e)

def hostTemplateMaps(domain):
    return dict({
        "{domain}": domain
    })

def mapping(text, dictionary):
    for i in dictionary:
        text = (text).replace(i,dictionary[i])
    return text

def __validUrl(url):
    """

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
    try:
        if not emailValidator(email) :
            error('__validEmail from helper file',"Correct Email: ex@example.com")
        return email
    except Exception as e:
        error('__validEmail from helper file', e)

def error(From, msg , DEBUG = configs.DEBUG):
    if DEBUG:
        logging.error("EXCEPTION [{}] - {}".format(From,msg))
    else:
        logging.error("{}".format(msg))
    exit(2)

def info(msg):
    print("[*] {}".format(msg))