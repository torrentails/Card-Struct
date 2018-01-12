#!/usr/bin/python3

from . import _version_check

# import

from . import logger

__all__ = ['log']

__author__  = "Nathan Sullivan <nsul@torrentails.com>"
__status__  = "development"
__version__ = "0.0.1.0"
__date__    = "13 Janurary 2018"


_log = logger.getLogger(__name__)
log = logger.getLogger('__main__')

if __name__ == '__main__':
    pass
