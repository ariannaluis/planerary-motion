"""
Functions to run simulations of celestial bodies' motion using numerical integration
methods.
"""

import numpy as np
from src.equations import euler_method


def simulate_two_body(t_span, dt, initial_conditions, masses):
    n_steps = int(t_span / dt)
    x_positions = [initial_conditions[0]]
    y_positions = [initial_conditions[1]]
    state = np.array(initial_conditions)

    for _ in range(n_steps):
        state = euler_method(state, masses, dt)
        x_positions.append(state[0])
        y_positions.append(state[1])

    return np.array(x_positions), np.array(y_positions)


def simulate_three_body(t_span, dt, initial_conditions, masses):
    n_steps = int(t_span / dt)
    x1_positions = [initial_conditions[0]]
    y1_positions = [initial_conditions[1]]
    x2_positions = [initial_conditions[4]]
    y2_positions = [initial_conditions[5]]
    x3_positions = [initial_conditions[8]]
    y3_positions = [initial_conditions[9]]
    state = np.array(initial_conditions)

    for _ in range(n_steps):
        state = euler_method(state, masses, dt)
        x1_positions.append(state[0])
        y1_positions.append(state[1])
        x2_positions.append(state[4])
        y2_positions.append(state[5])
        x3_positions.append(state[8])
        y3_positions.append(state[9])

    return (np.array(x1_positions), np.array(y1_positions),
            np.array(x2_positions), np.array(y2_positions),
            np.array(x3_positions), np.array(y3_positions))