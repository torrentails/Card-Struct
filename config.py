#!/usr/bin/python3

import logging
import time

class BASIC:
    name = "Card Struct"
    min_major_version = 3
    min_minor_version = 2

class LOGGING:
    log_level = logging.DEBUG
    file_emit_level = logging.DEBUG
    stream_emit_level = logging.INFO

    log_file = "{}.log".format(time.strftime("%y%m%d-%H%M%S"))

    emit_style = '{'
    emit_format = "{asctime:s} {levelname:s} {name:s}:{lineno:d} {message:s}"
    emit_date_format = "%H:%M:%S"
