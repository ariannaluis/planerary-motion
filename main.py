import numpy as np
from src.data_loader import load_masses, load_orbital_params
from src.simulation import simulate_two_body, simulate_three_body
from src.plotter import plot_positions, plot_orbits

G = 6.67430e-11  # gravitational constant


def main():
    masses = load_masses()
    orbital_params = load_orbital_params()

    # Choose terrestrial planet (example: Earth)
    planet = "earth"
    mass_sun = masses["sun"]
    mass_planet = masses[planet]
    mass_jupiter = masses["jupiter"]

    perihelion = orbital_params[planet]["perihelion"]
    aphelion = orbital_params[planet]["aphelion"]
    period = orbital_params[planet]["period"]

    semi_major_axis = (perihelion + aphelion) / 2

    # Initial conditions at perihelion
    x_planet = perihelion
    y_planet = 0
    vx_planet = 0
    vy_planet = np.sqrt(G * mass_sun * (2 / perihelion - 1 / semi_major_axis))

    initial_conditions_two_body = [x_planet, y_planet, vx_planet, vy_planet, 0, 0, 0, 0]
    t_span_two_body = (0, 3 * period)
    dt = 60 * 60  # 1 hour time step

    # Simulate two-body system (Sun and terrestrial planet)
    times, positions = simulate_two_body(
        [mass_planet, mass_sun], initial_conditions_two_body, t_span_two_body, dt
    )

    # Plot results
    plot_positions(
        times, [positions[0], positions[1]], ["x_earth", "y_earth"], "Position vs Time (Two-Body System)"
    )
    plot_orbits(
        [[positions[0], positions[1]]], ["Earth"], "Orbit Trace (Two-Body System)"
    )

    # Initial conditions for three-body system at perihelion
    x_jupiter = orbital_params["jupiter"]["perihelion"]
    y_jupiter = 0
    vx_jupiter = 0
    vy_jupiter = np.sqrt(G * mass_sun * (2 / x_jupiter - 1 / orbital_params["jupiter"]["aphelion"]))

    # Sun's initial conditions (assuming stationary Sun)
    x_sun, y_sun = 0, 0
    vx_sun, vy_sun = 0, 0

    initial_conditions_three_body = [
        x_planet, y_planet, vx_planet, vy_planet,
        x_jupiter, y_jupiter, vx_jupiter, vy_jupiter,
        x_sun, y_sun, vx_sun, vy_sun
    ]
    t_span_three_body = (0, 36 * period)

    # Simulate three-body system (Sun, terrestrial planet, and Jupiter)
    times, positions = simulate_three_body(
        [mass_planet, mass_jupiter, mass_sun], initial_conditions_three_body, t_span_three_body, dt
    )

    # Plot results
    plot_positions(
        times, [positions[0], positions[1], positions[4], positions[5]],
        ["x_earth", "y_earth", "x_jupiter", "y_jupiter"], "Position vs Time (Three-Body System)"
    )
    plot_orbits(
        [[positions[0], positions[1]], [positions[4], positions[5]]],
        ["Earth", "Jupiter"], "Orbit Traces (Three-Body System)"
    )


if __name__ == "__main__":
    main()
