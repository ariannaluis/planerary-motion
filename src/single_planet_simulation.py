"""
Simulation for a single terrestrial object orbiting the Sun
"""

import json

with open('../data/planetary_data.json', 'r') as f:
    data = json.load(f)

G = data['constants']['G']


def gravitational_acceleration(x, y, M_sun):
    """
    Calculates the gravitational acceleration
    :param x:
    :param y:
    :param M_sun:
    :return:
    """
    return 0


def euler_step(x, y, vx, vy, ax, ay, dt):
    """
    Performs one step of the Euler method
    :param x:
    :param y:
    :param vx:
    :param vy:
    :param ax:
    :param ay:
    :param dt:
    :return:
    """
    return 0


if __name__ == "__main__":
    # load data from planetary_data.json
    # compute initial conditions using utils.py
    # run simulation for 3 years
    # store positions
    # plot results
    holder = None
