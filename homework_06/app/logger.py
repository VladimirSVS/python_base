import logging


DEFAULT_FORMAT = """%(asctime)s %(levelname)-8s [%(name)-8s] (%(filename)s:%(funcName)s:%(lineno)d) %(message)s"""
logging.basicConfig(format=DEFAULT_FORMAT, level=logging.DEBUG)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger