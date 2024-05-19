from src.simulation import simulate_two_body
import numpy as np

G = 6.67430e-11  # gravitational constant

mass_sun = 1.989e30  # kg
mass_earth = 5.972e24  # kg

perihelion = 147.09e9  # m
semi_major_axis = 149.60e9  # m
period = 365.25 * 24 * 3600  # s

x_earth = perihelion
y_earth = 0
vx_earth = 0
vy_earth = np.sqrt(G * mass_sun * (2 / perihelion - 1 / semi_major_axis))

initial_conditions = [x_earth, y_earth, vx_earth, vy_earth, 0, 0, 0, 0]
t_span = (0, period / 10)
dt = 24 * 3600

times, positions = simulate_two_body([mass_earth, mass_sun], initial_conditions, t_span, dt)
print("Simulation complete.")
print(f"Times: {times}")
print(f"Positions: {positions}")