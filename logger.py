# Copyright (C) 2018  Nathan Sullivan

import logging, time

from .config import LOGGING


class _MSec_Formatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            if "%F" in datefmt:
                msec = "%03d" % record.msecs
                datefmt = datefmt.replace("%F", msec)
            s = time.strftime(datefmt, ct)
        else:
            t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            s = "%s,%03d" % (t, record.msecs)
        return s


def getLogger(name, level=None, file_level=None, stream_level=None):
    try:
        log.debug("adding logger %s (%d, %d, %d)", name,
            level, file_level, stream_level)
    except NameError:
        pass # Defining the logger for the logging module

    logger = logging.getLogger(name)
    if level is None:
        logger.setLevel(LOGGING.log_level)
    else:
        logger.setLevel(level)

    fh = logging.FileHandler(LOGGING.log_file)
    if file_level is None:
        fh.setLevel(LOGGING.file_emit_level)
    else:
        fh.setLevel(LOGGING.file_emit_level)

    ch = logging.StreamHandler()
    if stream_level is None:
        ch.setLevel(LOGGING.stream_emit_level)
    else:
        ch.setLevel(LOGGING.stream_emit_level)

    formatter = logging.Formatter(LOGGING.emit_format,
        LOGGING.emit_date_format,
        LOGGING.emit_style)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


log = getLogger(__name__)
log.debug("logging initialised.")
