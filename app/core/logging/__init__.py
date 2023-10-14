import logging
from typing import List

from loguru import logger

LOG_LEVEL_INFO = logging.INFO
LOG_LEVEL_DEBUG = logging.DEBUG
LOG_LEVEL_WARNING = logging.WARNING
LOG_LEVEL_ERROR = logging.ERROR
LOG_LEVEL_CRITICAL = logging.CRITICAL


class LoguruHandler(logging.Handler):
    def emit(self, record):
        level = logger.level(record.levelname).name
        logger.opt(
            depth=6, exception=record.exc_info).log(level, record.getMessage())


def load_logging_handlers(packages: List[str], level=logging.INFO):
    for package in packages:
        _logger = logging.getLogger(package)
        _logger.setLevel(level)
        for handler in list(_logger.handlers):
            _logger.removeHandler(handler)
        _logger.addHandler(LoguruHandler())
