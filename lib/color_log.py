import logging
import sys


def color(col='BLUE'):

    table = {
        'BLUE': '\x1b[36;1m',
        'GREEN': '\x1b[32;1m',
        'YELLOW': '\x1b[33;1m',
        'RED': '\x1b[31;1m',
        'CRIT': '\x1b[33;41;1m'
    }
    sufix = '\x1b[39;49;0m'
    def _color(function):
        def __color(*args, **kw):
            sys.stdout.write(table[col])
            sys.stdout.flush()
            function(*args, **kw)
            sys.stdout.write(sufix)
            sys.stdout.flush()
            return
        return __color
    return _color


class ColorLog(object):

    def __init__(self, level=logging.INFO):
        fmt = '%(asctime)s %(name)s [%(levelname)s] <line:%(lineno)s> :%(message)s'
        logging.basicConfig(format=fmt,
                            datefmt='%Y/%m/%d %p %I:%M:%S',
                            level=level)

    @color('GREEN')
    def info(self, msg):
        logging.info(msg)

    @color('BLUE')
    def debug(self, msg):
        logging.debug(msg)

    @color('YELLOW')
    def warning(self, msg):
        logging.warning(msg)

    @color('RED')
    def error(self, msg):
        logging.error(msg)

    @color('CRIT')
    def critical(self, msg):
        logging.critical(msg)
