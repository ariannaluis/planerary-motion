import numpy as np
from src.data_loader import load_masses, load_orbital_params

body_masses = load_masses()
orbital_params = load_orbital_params()

G = 6.67430e-11  # gravitational constant
m_sun = body_masses["sun"]


def gravitational_acceleration(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    ax = -G * m_sun * x / r ** 3
    ay = -G * m_sun * y / r ** 3
    return ax, ay


def euler_method(x, y, vx, vy, dt):
    ax, ay = gravitational_acceleration(x, y)
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    return x, y, vx, vy


def gravitational_force(m1, m2, r):
    """
    Compute the gravitational force between two masses
    :param m1:  (float) mass of the first body
    :param m2:  (float) mass of the second body
    :param r:   (array) distance vector between the two bodies
    :return:    (array) gravitational force vector
    """
    force = G * m1 * m2 / np.linalg.norm(r) ** 3 * r
    print(f"Gravitational force: {force} for r: {r}")
    return force


def differential_equations(t, y, masses):
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


def euler_method(state, masses, dt):
    """
    Define difference equations for the motion of celestial bodies
    :param state:   (array) state vector containing positions and velocities
    :param masses:  (list)  list of masses of the bodies
    :param dt:      (float) time step for the simulation
    :return:        (list)  updated state vector after one time step
    """
    n = len(masses)
    positions = state[:2 * n].reshape((n, 2))
    velocities = state[2 * n:].reshape((n, 2))

    dx = positions[:, 0].reshape(n, 1) - positions[:, 0]
    dy = positions[:, 1].reshape(n, 1) - positions[:, 1]
    dist_squared = dx ** 2 + dy ** 2
    dist_cubed = dist_squared ** 1.5

    np.fill_diagonal(dist_cubed, np.inf)

    ax = G * np.sum(dx * masses / dist_cubed, axis=1)
    ay = G * np.sum(dy * masses / dist_cubed, axis=1)

    velocities[:, 0] += ax * dt
    velocities[:, 1] += ay * dt

    positions[:, 0] += velocities[:, 0] * dt
    positions[:, 1] += velocities[:, 1] * dt

    new_state = np.zeros_like(state)
    new_state[:2 * n] = positions.flatten()
    new_state[2 * n:] = velocities.flatten()

    return new_state
