import numpy as np


class Vec2D:

    def __init__(self, x, y):
        self.__x, self.__y = x, y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def add(self, other):
        if isinstance(other, Vec2D):
            new_x = self.x + other.__x
            new_y = self.y + other.__y
        else:
            raise TypeError(f'{other} should be of type {type(Vec2D)}')
        return new_x, new_y

    def __add__(self, other):
        new_x, new_y = self.add(other)
        return Vec2D(new_x, new_y)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iadd__(self, other):
        self.__x, self.__y = self.add(other)
        return self

    def sub(self, other):
        if isinstance(other, Vec2D):
            new_x = self.x - other.__x
            new_y = self.y - other.__y
        else:
            raise TypeError(f'{other} should be of type {type(Vec2D)}')
        return new_x, new_y

    def __sub__(self, other):
        new_x, new_y = self.sub(other)
        return Vec2D(new_x, new_y)

    def __isub__(self, other):
        self.__x, self.__y = self.sub(other)
        return self

    def __str__(self):
        return f'x = {self.__x}, y = {self.__y}'

    def __repr__(self):
        return self.__str__()

    def dp(self, other):
        if isinstance(other, Vec2D):
            xx = self.__x * other.__x
            yy = self.__y * other.__y
        else:
            raise TypeError(f'{other} should be of type {type(Vec2D)}')
        return xx + yy

    def length(self):
        return np.sqrt(self.dp(self))

    def scale_inplace(self, scale_factor):
        self.__x = self.__x * scale_factor
        self.__y = self.__y * scale_factor
        return self

    def scale(self, scale_factor):
        new_x = self.__x * scale_factor
        new_y = self.__y * scale_factor
        return Vec2D(new_x, new_y)

    def normalize(self):
        l = self.length()
        assert l != 0, 'Vector of 0 length can not be normalized to unit length'
        return self.scale(1 / l)


def point_on_segment_projection(point: Vec2D, vec1: Vec2D, vec2: Vec2D):
    line_segment = vec2 - vec1
    t = ((point.x - vec1.x) * (vec2.x - vec1.x) + (point.y - vec1.y)
         * (vec2.y - vec1.y)) / line_segment.length() ** 2
    new_point = line_segment.scale(t) + vec1
    perpendicular_vector = new_point - point
    return perpendicular_vector, t
