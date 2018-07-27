import logging

from ApacheLocalDomain.app import configs

logging.basicConfig(format='[E] %(message)s', level=logging.ERROR)


def error(From, msg, DEBUG=configs.DEBUG):
    if DEBUG:
        logging.error("EXCEPTION [{}] - {}".format(From, msg))
    else:
        logging.error("{}".format(msg))
    exit(-1)


def info(msg):
    print("[*] {}".format(msg))
