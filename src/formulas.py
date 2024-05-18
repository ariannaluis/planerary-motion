import numpy as np
from data.constants import G


def gravitational_force(m1, m2, r1, r2):
    """
    Calculate gravitational force between two masses

    :param m1: (float) mass of first body
    :param m2: (float) mass of second body
    :param r1: (numpy array) position vector of first body
    :param r2: (numpy array) position vector of second body

    :return: force (numpy array) : gravitational force on m1 due to m2 (Newtons)
    """
    r = r2 - r1                     # displacement vector from r1 to r2
    distance = np.linalg.norm(r)    # magnitude of displacement vector

    force_magnitude = (G * m1 * m2) / (distance ** 2)   # magnitude of gravitational force
    force = force_magnitude * r     # directional force vector

    return force


def acceleration(force, mass):
    """
    Calculate acceleration of a body given the force acting on it and its mass

    :param force: (numpy array) force vector (Newtons)
    :param mass: (float) mass of the body (kg)

    :return: acceleration (numpy array) : acceleration vector (m/s^2)
    """
    return force / mass                 #acceleration = force/mass


def update_position(position, velocity, dt):
    """
    Update position of a body given its velocity and change in time

    :param position: (numpy array) current position vector (m)
    :param velocity: (numpy array) current velocity vector (m/s)
    :param dt: (float) change in time (s)

    :return: new_position (numpy array) : updated position vector (m)
    """
    return position + velocity * dt     # new position = old position + velocity * dt


def update_velocity(velocity, accel, dt):
    """
    Update velocity of a body given its acceleration and change in time

    :param velocity: (numpy array) current velocity vector (m/s)
    :param accel: (numpy array) current acceleration vector (m/s^2)
    :param dt: (float) change in time (s)

    :return: new_velocity (numpy array) : updated velocity vector (m/s)
    """
    return velocity + accel * dt        # new velocity = velocity + acceleration * dt
