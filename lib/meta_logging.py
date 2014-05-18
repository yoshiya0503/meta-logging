#!/usr/bin/env python
import logging


def log(level=logging.DEBUG):
    """
    in the case of debug mode,
    output log for all class and method decorated
    """
    print "\x1b[32mSTART DEBUG MODE"

    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')

    def decorator(klass):
        def logger(function):
            def wrap(*args, **kw):
                logging.debug('... [class : method] ===> [%s : %s]' % (klass.__name__, function.func_name))
                return function(*args, **kw)
            return wrap

        for el in dir(klass):
            if el.startswith('_'):
                continue
            value = getattr(klass, el)

            if not hasattr(value, 'im_func'):
                continue
            setattr(klass, el, logger(value))
        return klass
    return decorator
