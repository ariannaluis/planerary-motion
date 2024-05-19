"""
Simulates the motion of a terrestrial planet and Jupiter under the gravitational
influence of the Sun.
Uses numerical methods to solve the differential equations governing the motion of
these celestial bodies.
"""

import os
import json
import numpy as np
from src.data_loader import load_masses, load_orbital_params
from src.simulation import simulate_two_body, simulate_three_body
from src.plotter import plot_positions, plot_orbits, save_plot

G = 6.67430e-11  # gravitational constant


def save_data(file_path, times, positions):
    """
    Save simulation data to a JSON file
    :param file_path:   (str)   path to the JSON file
    :param times:       (array) array of time points
    :param positions:   (array) array of positions for the bodies
    """
    data = {
        'times': times.tolist(),
        'positions': [pos.tolist() for pos in positions]
    }
    with open(file_path, 'w') as f:
        json.dump(data, f)


def main():
    """
    Main function of the simulation
    """
    # make sure results directories exist
    os.makedirs('results/data', exist_ok=True)
    os.makedirs('results/plots', exist_ok=True)

    # load masses and orbital parameters from JSON files
    masses = load_masses()
    orbital_params = load_orbital_params()

    # choose terrestrial planet and get relevant data
    planet = "earth"
    mass_sun = masses["sun"]
    mass_planet = masses[planet]
    mass_jupiter = masses["jupiter"]

    # get parameters for planet
    perihelion = orbital_params[planet]["perihelion"] * 1e3
    aphelion = orbital_params[planet]["aphelion"] * 1e3
    period = orbital_params[planet]["period"]
    semi_major_axis = orbital_params[planet]["semi_major_axis"] * 1e3

    # initial conditions at perihelion for two-body system
    x_planet = perihelion
    y_planet = 0
    vx_planet = 0
    vy_planet = np.sqrt(G * mass_sun * (2 / perihelion - 1 / semi_major_axis))

    # debug: print initial conditions for two-body problem
    print(f"Initial conditions for two-body problem: x_planet={x_planet}, "
          f"y_planet={y_planet}, vx_planet={vx_planet}, vy_planet={vy_planet}")

    # initial state vector for two-body system
    # [x1, y1, vx1, vy1, x2, y2, vx2, vy2]
    initial_conditions_two_body = [x_planet, y_planet,
                                   vx_planet, vy_planet,
                                   0, 0, 0, 0]
    t_span_two_body = (0, 3 * period)  # simulate for 3 years
    dt = 60 * 60  # 1 hour time step

    # simulate two-body system (sun and terrestrial planet)
    times, positions = simulate_two_body([mass_planet, mass_sun],
                                         initial_conditions_two_body,
                                         t_span_two_body, dt)

    # save data for two-body system
    save_data('results/data/two_body.json', times, positions)

    # plot results
    plot_positions(times, [positions[0], positions[1]], ["x_earth", "y_earth"],
                   "Position vs Time (Two-Body System)")
    save_plot('results/plots/two_body_position_vs_time.png')
    plot_orbits([[positions[0], positions[1]]], ["Earth"],
                "Orbit Trace (Two-Body System)")
    save_plot('results/plots/two_body_orbit_trace.png')

    # initial conditions at perihelion for three-body system
    semi_major_axis_jupiter = orbital_params["jupiter"]["semi_major_axis"] * 1e3
    x_jupiter = orbital_params["jupiter"]["perihelion"] * 1e3
    y_jupiter = 0
    vx_jupiter = 0
    vy_jupiter = np.sqrt(G * mass_sun * (2 / x_jupiter - 1 / semi_major_axis_jupiter))

    # debug: print initial conditions for three-body system
    print(f"Initial conditions for three-body problem: x_jupiter={x_jupiter}, "
          f"y_jupiter={y_jupiter}, vx_jupiter={vx_jupiter}, vy_jupiter={vy_jupiter}")

    # sun's initial conditions (assuming stationary sun)
    x_sun, y_sun = 0, 0
    vx_sun, vy_sun = 0, 0

    # initial state vector for three-body problem
    # [x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3]
    initial_conditions_three_body = [
        x_planet, y_planet, vx_planet, vy_planet,
        x_jupiter, y_jupiter, vx_jupiter, vy_jupiter,
        x_sun, y_sun, vx_sun, vy_sun
    ]
    t_span_three_body = (0, 36 * period)

    # simulate three-body system (sun, terrestrial planet, and jupiter)
    times, positions = simulate_three_body([mass_planet, mass_jupiter, mass_sun],
                                           initial_conditions_three_body,
                                           t_span_three_body, dt)

    # save data for three-body system
    save_data('results/data/three_body.json', times, positions)

    # plot results
    plot_positions(times, [positions[0], positions[1], positions[4], positions[5]],
                   ["x_earth", "y_earth", "x_jupiter", "y_jupiter"],
                   "Position vs Time (Three-Body System)")
    save_plot('results/plots/three_body_position_vs_time.png')
    plot_orbits([[positions[0], positions[1]], [positions[4], positions[5]]],
                ["Earth", "Jupiter"],
                "Orbit Traces (Three-Body System)")
    save_plot('results/plots/three_body_orbit_trace.png')


if __name__ == "__main__":
    main()
