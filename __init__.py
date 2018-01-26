# Card Struct
# Copyright (C) 2018  Nathan Sullivan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from . import _version_check
from . import Logger as _logger
from . import Controller
# from .config import BASIC

# __all__ = ['All', 'G',
#     'card', 'frame', 'geometry', 'logger']

__author__  = "Nathan Sullivan <nsul@torrentails.com>"
__status__  = "development"
__version__ = "0.0.13"
__date__    = "18 Janurary 2018"


_log = _logger.init(__name__)

G = Controller.init()

from .Card import *
from .Geometry import *
from .Frame import *


class _AllType:
    inst = None
    def __new__(cls, *args, **kwargs):
        if cls.inst is None:
            cls.inst = type('AllType', (object,), {})()
        return cls.inst

    def __setattr__(self, name, value):
        raise AttributeError("'{}' object has no attribute '{}'" \
            .format(self.__class__.__name__, name))

All = _AllType()


if __name__ == '__main__':
    #TODO: run tests here
    pass
