"""
Functions to run simulations of celestial bodies' motion using numerical integration
methods.
"""

import numpy as np
from scipy.integrate import solve_ivp
from .equations import differential_equations, difference_equations


def simulate_two_body(masses, initial_conditions, t_span, dt):
    """
    Simulate the motion of a two-body system.
    :param masses:              (list)  list of masses of the bodies
    :param initial_conditions:  (list)  initial state vector
                                        [x1, y1, vx1, vy1, x2, y2, vx2, vy2]
    :param t_span:              (tuple) time span for the simulation (start, end)
    :param dt:                  (float) time step for the simulation
    :return:                    (tuple) times and positions of the celestial bodies
    """
    # times at which to store results
    t_eval = np.arange(t_span[0], t_span[1], dt)

    # solve differential equations using solve_ivp
    solution = solve_ivp(
        differential_equations, t_span, initial_conditions, args=(masses,), t_eval=t_eval, method='RK45'
    )

    return solution.t, solution.y


def simulate_three_body(masses, initial_conditions, t_span, dt):
    """
    Simulate the motion of a three-body system
    :param masses:              (list)  list of masses of the bodies
    :param initial_conditions:  (list)  initial state vector
                                        [x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3]
    :param t_span:              (tuple) time span for the simulation (start, end)
    :param dt:                  (float) time step for the simulation
    :return:                    (tuple) times and positions of the celestial bodies
    """
    # times at which to store results
    t_eval = np.arange(t_span[0], t_span[1], dt)

    # solve differential equations using solve_ivp
    solution = solve_ivp(
        differential_equations, t_span, initial_conditions, args=(masses,), t_eval=t_eval, method='RK45'
    )

    return solution.t, solution.y


def run_difference_simulation(masses, initial_conditions, t_span, dt):
    """
    Simulate the motion of bodies using difference equations
    :param masses:              (list)  list of masses of the bodies
    :param initial_conditions:  (list)  initial state vector
    :param t_span:              (tuple) time span for the simulation (start, end)
    :param dt:                  (float) time step for the simulation
    :return:                    (array) trajectory of the bodies
    """
    # calculate number of steps
    num_steps = int((t_span[1] - t_span[0]) / dt)
    state = initial_conditions

    # initialize array to store trajectory
    trajectory = np.zeros((num_steps, len(state)))

    # iterate through time steps
    for step in range(num_steps):
        trajectory[step] = state
        state = difference_equations(state, masses, dt)

    return trajectory
