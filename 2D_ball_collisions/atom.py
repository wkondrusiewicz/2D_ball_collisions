from vec2d import Vec2D


class Atom(Vec2D):
    def __init__(self, mass: float = 1., velocity: Vec2D = Vec2D(0, 0), position: Vec2D = Vec2D(0, 0), radius: float = 0.):
        super().__init__(position.x, position.y)
        self.__mass = mass
        self.__velocity = velocity
        self.__position = position
        self.__radius = radius

    def __str__(self):
        return f'position: {self.__position} with radius of {self.__radius}'

    def __repr__(self):
        return self.__str__()

    @property
    def mass(self):
        return self.__mass

    @property
    def velocity(self):
        return self.__velocity

    @property
    def position(self):
        return self.__position

    @property
    def radius(self):
        return self.__radius

    @mass.setter
    def mass(self, mass):
        self.___mass = mass

    @position.setter
    def position(self, position):
        self.__position = position

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    @radius.setter
    def radius(self, radius):
        self.__radius = radius
