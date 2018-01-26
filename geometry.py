# Copyright (C) 2018  Nathan Sullivan

import math
from . import Logger


log = Logger.getChildLogger(__name__)


def line_point(x1, y1=None, x2=None, y2=None, ratio=0.5):
    """ Returns (x, y) where x and y are coordinates of a point that lies on the
        line [(x1, y1), (x2, y2)] with respect to the ratio.

        Parameters:
            x1, y1, x2, y2: Floats or ints defining the line
            ratio: A float from 0.0 to 1.0 the ratio defining how far along the
                line to get the point

        Returns:
            (float, float): Coordinates such that when ratio is 0.0, (x1, y1)
                will be returned and when ratio is 1.0, (x2, y2) will be
                returned. The default ratio will return the point half-way
                between (x1, y1) and (x2, y2)

        Note: x1, y1, x2, y2 can be (almost) any combination of numbers and/or
            iterables and the system will attempt to extract the correct
            values. Because of this, it is recommended to always pass ratio
            explicitly.
    """
    log.debug("Getting point from coords. (%s, %s, %s, %s, %f)",
        x1, y1, x2, y2, ratio)
    x1, y1, x2, y2 = _get_four_points(x1, y1, x2, y2)
    return (x2-x1)*ratio+x1, (y2-y1)*ratio+y1

def _get_four_points(x1, y1=None, x2=None, y2=None):
    log.debug("Getting four points. (%s, %s, %s, %s)",
        x1, y1, x2, y2)
    if issubclass(type(x1), Vec4) or \
        hasattr(x1, '__iter__') and len(x1) == 4:
        x1, y1, x2, y2 = x1[0], x1[1], x1[2], x1[3]

    elif issubclass(type(x1), Vec2) and issubclass(type(y1), Vec2):
        x2, y2 = y1.x, y1.y
        x1, y1 = x1.x, x1.y

    elif issubclass(type(x1), Vec2):
        y2 = x2
        x2 = y1
        y1 = x1.y
        x1 = x1.x

    elif (i for i in (x1, y1, x2, y2) if isinstance(i, (int, float))):
        pass

    else:
        raise TypeError("Unknown types to extract points", x1, y1, x2, y2)

    return x1, y1, x2, y2


class _Vec:
    def __init__(self, x, y):
        log.debug("New %s object", self.__class__)
        self.x = x
        self.y = y

    @property
    def x1(self):
        return self.x
    @x1.setter
    def x1(self, x):
        self.x = x

    @property
    def y1(self):
        return self.y
    @y1.setter
    def y1(self, y):
        self.y = y

    def __iter__(self):
        for val in (self.x, self.y):
            yield val


class Vec2(_Vec):
    def __init__(self, x, y=None):
        if y is None:
            y = x[1]
            x = x[0]
        super().__init__(x, y)

    def __len__(self):
        return 2

# class point(Vec2, _rendered):
#     pass # render code here


class Vec4(_Vec):
    def __init__(self, x1, y1=None, x2=None, y2=None):
        x1, y1, x2, y2 = _get_four_points(x1, y1, x2, y2)
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2

    @property
    def length(self):
        return math.sqrt(abs(self.x1-self.x2)**2 + abs(self.y1-self.y2)**2)

    def start_point(self):
        return Vec2(self.x1, self.y1)

    def end_point(self):
        return Vec2(self.x2, self.y2)

    def mid_point(self):
        return Vec2(line_point(self, p=0.5))

    # def __getitem__(self, index):

    def __iter__(self):
        for val in (self.x1, self.y1, self.x2, self.y2):
            yield val

    def __len__(self):
        return 4


# class line(Vec4, _rendered):
#     pass # render code here
