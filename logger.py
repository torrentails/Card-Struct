# Copyright (C) 2018  Nathan Sullivan

import logging, os, platform, time

from .Config import BASIC, LOGGING


__all__ = ['getLogger', 'debug_dump']


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


def getLogger(name, level=None, file_level=None,
    stream_level=None, base_logger=True):
    if level is None:
        level = LOGGING.log_level
    if file_level is None:
        file_level = LOGGING.file_emit_level
    if stream_level is None:
        stream_level = LOGGING.stream_emit_level

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if base_logger:
        formatter = _MSec_Formatter(LOGGING.emit_format,
            LOGGING.emit_date_format,
            LOGGING.emit_style)

        if LOGGING.log_files_to_keep > 0:
            try:
                os.mkdir(os.path.dirname(LOGGING.log_file))
            except FileExistsError:
                pass

            fh = logging.FileHandler(LOGGING.log_file)
            fh.setLevel(LOGGING.file_emit_level)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(LOGGING.stream_emit_level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger


def getChildLogger(name, level=None, file_level=None, stream_level=None):
    if level is None:
        level = LOGGING.log_level
    if file_level is None:
        file_level = LOGGING.file_emit_level
    if stream_level is None:
        stream_level = LOGGING.stream_emit_level

    log.debug("adding logger %s (%d, %d, %d)", name,
        level, file_level, stream_level)

    return getLogger(name, level, file_level, stream_level, False)


def debug_dump():
    #TODO: emit debug logs here
    pass


def cleanup_old_logs():
    try:
        lst = [file for file in os.listdir(os.path.dirname(LOGGING.log_file))
            if file.endswith('.log')]

        if LOGGING.log_files_to_keep > 1:
            lst = lst[:-1*(LOGGING.log_files_to_keep-1)]
        for file in lst:
            os.remove(os.path.join(os.path.dirname(LOGGING.log_file), file))

    except FileNotFoundError:
        return


def init(name):
    cleanup_old_logs()

    global log

    _base_log = getLogger(name)
    _base_log.debug("%s %s-%s", BASIC.package_name, BASIC.version, BASIC.status)
    _base_log.debug("%s %s on %s %s %s (%s)", platform.python_implementation(),
        platform.python_version(), platform.system(), platform.release(),
        platform.version(), platform.machine())

    log = getLogger(__name__, base_logger=False)

    log.debug("logging initialised.")

    return _base_log
