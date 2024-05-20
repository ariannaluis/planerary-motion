"""
Functions to compute gravitational forces and differential equations for the motion
of celestial bodies.
"""

import cProfile
import numpy as np
from functools import lru_cache
from line_profiler import profile

G = 6.67430e-11  # gravitational constant


def arr_to_tuple(arr):
    return tuple(arr)


@profile
@lru_cache(maxsize=None)
def cached_gravitational_force(m1, m2, r_tuple):
    r = np.array(r_tuple)
    norm_r = np.linalg.norm(r)
    force = G * m1 * m2 / norm_r ** 3 * r
    return force


@profile
def gravitational_force(m1, m2, r):
    """
    Compute the gravitational force between two masses
    :param m1:  (float) mass of the first body
    :param m2:  (float) mass of the second body
    :param r:   (array) distance vector between the two bodies
    :return:    (array) gravitational force vector
    """
    r_tuple = arr_to_tuple(r)
    return cached_gravitational_force(m1, m2, r_tuple)


@profile
def differential_equations(t, y, masses):
    """
    Define differential equations for the motion of bodies
    :param t:       (float) current time
    :param y:       (array) current state vector containing positions and velocities
    :param masses:  (list)  list of masses of the bodies
    :return:        (list)  derivatives of the state vector
    """
    n = len(masses)
    positions = y[:2 * n].reshape((n, 2))
    velocities = y[2 * n:].reshape((n, 2))

    dydt = np.zeros_like(y)
    dydt[:2 * n] = velocities.flatten()

    dx = positions[:, 0].reshape(n, 1) - positions[:, 0]
    dy = positions[:, 1].reshape(n, 1) - positions[:, 1]
    dist_squared = dx ** 2 + dy ** 2
    dist_cubed = dist_squared ** 1.5

    np.fill_diagonal(dist_cubed, np.inf)

    ax = G * np.sum(dx * masses / dist_cubed, axis=1)
    ay = G * np.sum(dy * masses / dist_cubed, axis=1)

    dydt[2 * n:2 * n + 2 * n:2] = ax
    dydt[2 * n + 1:2 * n + 2 * n:2] = ay

    return dydt


@profile
def difference_equations(state, masses, dt):
    """
    Define difference equations for the motion of celestial bodies
    :param state:   (array) state vector containing positions and velocities
    :param masses:  (list)  list of masses of the bodies
    :param dt:      (float) time step for the simulation
    :return:        (list)  updated state vector after one time step
    """
    # two-body case
    if len(masses) == 2:
        # unpack state vector
        x1, y1, vx1, vy1, x2, y2, vx2, vy2 = state
        m1, m2 = masses

        # compute distance vectors between the bodies
        r12 = np.array([x2 - x1, y2 - y1])

        # compute accelerations due to gravitational forces
        a1 = gravitational_force(m2, m1, -r12) / m1
        a2 = gravitational_force(m1, m2, r12) / m2

        # update velocities and positions using difference equations
        vx1_new = vx1 + a1[0] * dt
        vy1_new = vy1 + a1[1] * dt
        vx2_new = vx2 + a2[0] * dt
        vy2_new = vy2 + a2[1] * dt

        x1_new = x1 + vx1_new * dt
        y1_new = y1 + vy1_new * dt
        x2_new = x2 + vx2_new * dt
        y2_new = y2 + vy2_new * dt

        return [x1_new, y1_new, vx1_new, vy1_new, x2_new, y2_new, vx2_new, vy2_new]

    # three-body case
    elif len(masses) == 3:

        # unpack state vector
        x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = state
        m1, m2, m3 = masses

        # compute distance vectors between the bodies
        r12 = np.array([x2 - x1, y2 - y1])
        r13 = np.array([x3 - x1, y3 - y1])
        r23 = np.array([x3 - x2, y3 - y2])

        # compute accelerations due to gravitational forces
        a1 = gravitational_force(m2, m1, -r12) / m1 + gravitational_force(m3, m1, -r13) / m1
        a2 = gravitational_force(m1, m2, r12) / m2 + gravitational_force(m3, m2, -r23) / m2
        a3 = gravitational_force(m1, m3, r13) / m3 + gravitational_force(m2, m3, r23) / m3

        # update velocities and positions using difference equations
        vx1_new = vx1 + a1[0] * dt
        vy1_new = vy1 + a1[1] * dt
        vx2_new = vx2 + a2[0] * dt
        vy2_new = vy2 + a2[1] * dt
        vx3_new = vx3 + a3[0] * dt
        vy3_new = vy3 + a3[1] * dt

        x1_new = x1 + vx1_new * dt
        y1_new = y1 + vy1_new * dt
        x2_new = x2 + vx2_new * dt
        y2_new = y2 + vy2_new * dt
        x3_new = x3 + vx3_new * dt
        y3_new = y3 + vy3_new * dt

        return [x1_new, y1_new, vx1_new, vy1_new, x2_new, y2_new, vx2_new, vy2_new, x3_new, y3_new, vx3_new, vy3_new]
