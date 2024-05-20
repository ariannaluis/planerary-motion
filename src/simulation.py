"""
Functions to run simulations of celestial bodies' motion using numerical integration
methods.
"""

import cProfile
import numpy as np
from scipy.integrate import solve_ivp
from src.equations import differential_equations, gravitational_force


def simulate_two_body(masses, initial_conditions, t_span, dt,
                      method='RK45', rtol=1e-8, atol=1e-8):
    """
    Simulate the motion of a two-body system.
    :param masses:              (list)  list of masses of the bodies
    :param initial_conditions:  (list)  initial state vector
                                        [x1, y1, vx1, vy1, x2, y2, vx2, vy2]
    :param t_span:              (tuple) time span for the simulation (start, end)
    :param dt:                  (float) time step for the simulation
    :param method:
    :param rtol:
    :param atol:
    :return:                    (tuple) times and positions of the celestial bodies
    """
    def wrapper(t, y):
        return differential_equations(t, y, masses)

    # times at which to store results
    t_eval = np.arange(t_span[0], t_span[1], dt)

    # solve differential equations using solve_ivp
    sol = solve_ivp(wrapper, t_span, initial_conditions,
                    t_eval=t_eval, method=method, rtol=rtol, atol=atol)

    # extract positions from solution
    positions = sol.y
    return sol.t, positions


def simulate_three_body(masses, initial_conditions, t_span, dt,
                        method='RK45', rtol=1e-5, atol=1e-8):
    """
    Simulate the motion of a three-body system
    :param masses:              (list)  list of masses of the bodies
    :param initial_conditions:  (list)  initial state vector
                                        [x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3]
    :param t_span:              (tuple) time span for the simulation (start, end)
    :param dt:                  (float) time step for the simulation
    :param method:
    :param rtol:
    :param atol:
    :return:                    (tuple) times and positions of the celestial bodies
    """
    def wrapper(t, y):
        return differential_equations(t, y, masses)

    # times at which to store results
    t_eval = np.arange(t_span[0], t_span[1], dt)

    # solve differential equations using solve_ivp
    sol = solve_ivp(wrapper, t_span, initial_conditions,
                    t_eval=t_eval, method=method, rtol=rtol, atol=atol)

    positions = sol.y
    return sol.t, positions
