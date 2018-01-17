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

# import

from . import logger

__all__ = ['log']

__author__  = "Nathan Sullivan <nsul@torrentails.com>"
__status__  = "development"
__version__ = "0.0.1.1"
__date__    = "13 Janurary 2018"


_log = logger.getLogger(__name__)
log = logger.getLogger('__main__')


class _G():
    def __init__(self):
        self.current_card = 0
        self.headers = None
        self.data = []

        self.card_ranges = {}

        self.cards_start = 0
        self.cards_end = 0

G = _G()

def All(obj):
    G.card_ranges[start] = (G.cards_start, G.cards_end)

def Range(start, stop=None):
    if type(start) is type(All):
        start = G.cards_start
        end = G.cards_end

    elif stop is None:

if __name__ == '__main__':
    pass
