# Copyright (C) 2018  Nathan Sullivan

import logging
import os
import time


__all__ = ['BASIC', 'LOGGING',]


class BASIC:
    author_name = "Nathan Sullivan"
    author_email = "nsul@torrentails.com"
    author = '%s <%s>' % (author_name, author_email)
    name = "Card Struct"
    package_name = "cardstruct"
    major = 0
    minor = 0
    patchlevel = 13
    status = 'development'
    version = '.'.join((str(major), str(minor), str(patchlevel)))
    min_python_major = 3
    min_python_minor = 2

class LOGGING:
    log_level = logging.DEBUG
    file_emit_level = logging.DEBUG
    stream_emit_level = logging.INFO

    log_directory = 'logs'
    log_file = os.path.join(log_directory,
        "%s%s.log" % (BASIC.package_name, time.strftime("%y%m%d%H%M%S")))
    log_files_to_keep = 5

    emit_style = '%'
    emit_format = "%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s"
    emit_date_format = "%H:%M:%S.%F"
