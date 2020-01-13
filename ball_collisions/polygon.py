from typing import List

from ball_collisions.atom import Atom
from ball_collisions.vec2d import Vec2D


class Polygon(Atom):

    def __init__(self, nodes: List[Vec2D] = []):
        super().__init__(position=get_center(nodes), radius=get_radius(nodes))
        self.__nodes = nodes

    @property
    def nodes(self):
        return self.__nodes

    def __str__(self):
        return super().__str__() + f' and {len(nodes)}'


def get_center(nodes: List[Vec2D] = []):
    if len(nodes) == 0:
        return Vec2D(0, 0)
    center_x, center_y = 0, 0
    for node in nodes:
        center_x += node.x
        center_y += node.y
    return Vec2D(center_x / len(nodes), center_y / len(nodes))


def get_radius(nodes: List[Vec2D] = []):
    center = get_center(nodes)
    return max([(node.x - center.x)**2 + (node.y - center.y)**2 for node in nodes])
