import os

from itertools import combinations

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from ball_collisions.atom import Atom
from ball_collisions.vec2d import Vec2D, point_on_segment_projection
from ball_collisions.polygon import Polygon
from ball_collisions.system import System


def get_new_velocity_after_wall_collision(atom, n_vec):
    atom_vel = atom.velocity
    u_vel = n_vec.scale(n_vec.dp(atom_vel) / n_vec.length()**2)
    w_vel = atom_vel - u_vel
    atom_vel_n = w_vel - u_vel
    return atom_vel_n


def get_f_coefficient(atom1, atom2):
    new_mass = atom1.mass + atom2.mass
    vel_diff = atom1.velocity - atom2.velocity
    pos_diff = atom1.position - atom2.position
    f = 2 * vel_diff.dp(pos_diff) / (new_mass * pos_diff.length() ** 2)
    return f


class Solver:

    def __init__(self, system, dt = 0.001):
        self.__system=system
        self.dt=dt
        self.__initial_positions=np.array(
            [[atom.position.x, atom.position.y] for atom in self.__system.atoms])

    def update_atoms_positions(self):
        for atom in self.__system.atoms:
            atom.position += atom.velocity.scale(self.dt)

    def atoms_walls_collisions(self):
        for atom in self.__system.atoms:
            for polygon in self.__system.display:
                for node1, node2 in zip(np.roll(polygon.nodes, 1), polygon.nodes):
                    perpendicular_vector, t=point_on_segment_projection(
                        atom.position, node1, node2)
                    if 0 < t < 1 and atom.radius >= perpendicular_vector.length():
                        atom.velocity=get_new_velocity_after_wall_collision(
                            atom, perpendicular_vector)
                        atom.position += atom.velocity.scale(self.dt)

    def atom_atom_collisons(self):
        for atom1, atom2 in combinations(self.__system.atoms, 2):
            pos_diff=atom1.position - atom2.position
            if atom1.radius + atom2.radius >= pos_diff.length():
                f=get_f_coefficient(atom1, atom2)
                atom1.velocity -= pos_diff.scale(atom2.mass * f)
                atom2.velocity += pos_diff.scale(atom1.mass * f)
                atom1.position += atom1.velocity.scale(self.dt)
                atom2.position += atom2.velocity.scale(self.dt)

    def single_run(self):
        self.atom_atom_collisons()
        self.atoms_walls_collisions()
        self.update_atoms_positions()

    def draw_system(self, iteration, figsize = (10, 10)):
        fig, ax=plt.subplots(figsize = figsize)

        # drawing atoms
        for i, atom in enumerate(self.__system.atoms):
            circle=plt.Circle(
                (atom.position.x, atom.position.y), atom.radius)
            ax.add_artist(circle)
            label = ax.annotate(f'{i}', xy = (atom.position.x, atom.position.y), fontsize =30, ha='center')
            ax.axis('off')
            ax.set_aspect('equal')
            ax.autoscale_view()

        # drawing borders
        for polygon in self.__system.display:
            borders=polygon.nodes
            for i in range(len(borders)):
                ax.add_line(mlines.Line2D([borders[i -1].x, borders[i].x], [borders[i -1].y, borders[i].y]))
        ax.set_title(f'Iteration = {iteration + 1}')
        os.makedirs('plots', exist_ok = True)
        plt.savefig(f'plots/img{iteration+1:06}.png')
        plt.close()

    def run_system(self, total_iterations = 1000):
        for i in range(total_iterations):
            self.draw_system(iteration = i)
            self.single_run()

#first copy `plots` directory to main (SSD) storage
# ffmpeg -framerate 60 -i img%06d.png output.mp4
