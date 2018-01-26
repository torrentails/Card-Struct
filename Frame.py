# Copyright (C) 2018  Nathan Sullivan

from . import Geometry, Logger


log = Logger.getChildLogger(__name__)


class Frame(Geometry.Vec4):
    def __init__(self, x, y, width, height, from_coords=False):
        if from_coords:
            x2 = width
            y2 = height
        else:
            x2 = x + width
            y2 = y + height
        super().__init__(x, y, x2, y2)

    @property
    def width(self):
        return self.x2 - self.x1
    @width.setter
    def width(self, width):
        self.x2 = self.x1 + width

    @property
    def height(self):
        return self.y2 + self.y1
    @height.setter
    def height(self, height):
        self.y2 = self.y1 - height


    def TL(self, xratio=0.0, yratio=None):
        if yratio is None:
            yratio = xratio
        x, _ = Geometry.line_point(self.x1, self.y1, self.x2, self.y2, xratio)
        _, y = Geometry.line_point(self.x1, self.y1, self.x2, self.y2, yratio)
        return Geometry.Vec2(x, y)

    def TR(self, xratio=0.0, yratio=None):
        if yratio is None:
            yratio = xratio
        x, _ = Geometry.line_point(self.x2, self.y1, self.x1, self.y2, xratio)
        _, y = Geometry.line_point(self.x2, self.y1, self.x1, self.y2, yratio)
        return Geometry.Vec2(x, y)

    def BL(self, xratio=0.0, yratio=None):
        if yratio is None:
            yratio = xratio
        x, _ = Geometry.line_point(self.x1, self.y2, self.x2, self.y1, xratio)
        _, y = Geometry.line_point(self.x1, self.y2, self.x2, self.y1, yratio)
        return Geometry.Vec2(x, y)

    def BR(self, xratio=0.0, yratio=None):
        if yratio is None:
            yratio = xratio
        x, _ = Geometry.line_point(self.x2, self.y2, self.x1, self.y1, xratio)
        _, y = Geometry.line_point(self.x2, self.y2, self.x1, self.y1, yratio)
        return Geometry.Vec2(x, y)
