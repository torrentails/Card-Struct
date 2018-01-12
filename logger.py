#!/usr/bin/python3

import inspect
import logging
import sys
import time
import warnings

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


def _deprecation(message, stacklevel=0):
    warnings.warn(message, DeprecationWarning, stacklevel=stacklevel+2)

# def _get_frame(depth=0):
#     function_name = None

#     try:
#         frame = inspect.currentframe()
#         if frame is not None:
#             if sys.version_info[0] <= 2:
#                 function_name = inspect.getouterframes(frame)[depth+1][3]
#             else:
#                 function_name = inspect.getouterframes(frame)[depth+1].function

#     finally:
#         del frame

#     return function_name


def getLogger(name:str, level:int=None, file_level:int=None,
    stream_level:int=None) -> logging.Logger:
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

# sys.stdout.write(string)
# sys.stderr.write(string)
