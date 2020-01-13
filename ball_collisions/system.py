from typing import List

from ball_collisions.atom import Atom
from ball_collisions.vec2d import Vec2D
from ball_collisions.polygon import Polygon

class System:

    def __init__(self, atoms: List[Atom] = [], display: List[Polygon] = []):
        self.__atoms = atoms
        self.__display = display

    def __str__(self):
        return f'Number of atoms in the systems = {len(self.__atoms)}, number of objects = {len(self.__display)}'

    @property
    def atoms(self):
        return self.__atoms

    @property
    def display(self):
        return self.__display

    def __repr__(self):
        return self.__str__()
