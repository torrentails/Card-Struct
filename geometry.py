import math

def _line_point(x1, y1=None, x2=None, y2=None, p=0.5):
    if type(x1) in (vec4, line):
        x1, y1, x2, y2 = x1.x1, x1.y1, x1.x2, x1.y2

    elif type(x1) in (vec2, point) and type(y1) in (vec2, point):
        x2, y2 = y1.x, y1.y
        x1, y1 = x1.x, x1.y

    elif type(x1) in (vec2, point):
        y2 = x2
        x2 = y1
        y1 = x1.y
        x1 = x1.x

    return abs(x1-x2)*p+min(x1, x2), abs(y1-y2)*p+min(y1,y2)


class _vec:
    def __init__(self, x, y):
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


class vec2(_vec):
    def __init__(self, x, y=None):
        if y is None:
            y = x[1]
            x = x[0]
        super().__init__(x, y)

class point(vec2):
    pass # render code here


class vec4(_vec):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2

    @property
    def length(self):
        return math.sqrt(abs(self.x1-self.x2)**2 + abs(self.y1-self.y2)**2)

    @property
    def start_point(self):
        return vec2(self.x1, self.y1)

    @property
    def end_point(self):
        return vec2(self.x2, self.y2)

    @property
    def mid_point(self):
        return vec2(_line_point(self, p=0.5))

class line(vec4):
    pass # render code here
