from color_log import ColorLog
import logging

log = ColorLog(level=logging.DEBUG)
log.info("hoge")
log.warning("hoge")
log.error("hoge")
log.debug("hoge")
log.critical("hoge")
