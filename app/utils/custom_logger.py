import logging

logger_format = '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s'


def setup_logger(logger_name=__name__, level=logging.INFO):
    log = logging.getLogger(logger_name)
    log.setLevel(level)
    if not log.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(logger_format)
        handler.setFormatter(formatter)
        log.addHandler(handler)
    return log
