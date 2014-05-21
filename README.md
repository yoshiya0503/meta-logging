meta-logging
============

logging tool for python using meta-programing

### quick start
    from meta_logging import log

    @log()
    class Hoge(object):

        def hoge(self):
            return 1 + 1

        def foo(self):
            return "foo"

    hoge = Hoge()
    hoge.hoge()   # => 2014-05-18 17:57:43,442 DEBUG ... [class : method] ===> [Hoge : hoge]
    hoge.foo()    # => 2014-05-18 17:57:43,442 DEBUG ... [class : method] ===> [Hoge : foo]

using color logging...

    from color_log import ColorLog
    import logging

    log = ColorLog(level=logging.DEBUG)
    log.info("hoge")
    log.warning("hoge")
    log.error("hoge")
    log.debug("hoge")
    log.critical("hoge")

### color logging sample
[!sample]('./sample/sample.png')
