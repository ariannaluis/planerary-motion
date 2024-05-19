import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from .equations import differential_equations, difference_equations


def simulate_two_body(masses, initial_conditions, t_span, dt):
    t_eval = np.arange(t_span[0], t_span[1], dt)
    solution = solve_ivp(
        differential_equations, t_span, initial_conditions, args=(masses,), t_eval=t_eval, method='RK45'
    )
    return solution.t, solution.y


def simulate_three_body(masses, initial_conditions, t_span, dt):
    t_eval = np.arange(t_span[0], t_span[1], dt)
    solution = solve_ivp(
        differential_equations, t_span, initial_conditions, args=(masses,), t_eval=t_eval, method='RK45'
    )
    return solution.t, solution.y


def run_difference_simulation(masses, initial_conditions, t_span, dt):
    num_steps = int((t_span[1] - t_span[0]) / dt)
    state = initial_conditions
    trajectory = np.zeros((num_steps, len(state)))
    for step in range(num_steps):
        trajectory[step] = state
        state = difference_equations(state, masses, dt)
    return trajectory
