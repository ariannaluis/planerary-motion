import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
m_sun = 1.989e30  # Mass of the Sun, kg
m_earth = 5.972e24  # Mass of the Earth, kg

# Initial conditions for Earth
x_earth = 147095000000.0  # Initial position in x, meters
y_earth = 0.0  # Initial position in y, meters
vx_earth = 0.0  # Initial velocity in x, meters/second
vy_earth = 30286.40277858803  # Initial velocity in y, meters/second

# Simulation parameters
t_span = 31558118.4  # One year in seconds
dt = 86400  # One day in seconds
n_steps = int(t_span / dt)

# Arrays to store the positions and velocities
x_positions = np.zeros(n_steps)
y_positions = np.zeros(n_steps)
vx = vx_earth
vy = vy_earth
x = x_earth
y = y_earth

# Euler's method for integration
for i in range(n_steps):
    r = np.sqrt(x**2 + y**2)
    ax = -G * m_sun * x / r**3
    ay = -G * m_sun * y / r**3
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    x_positions[i] = x
    y_positions[i] = y

# Plotting the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Position vs Time
ax1.plot(np.linspace(0, t_span, n_steps), x_positions, label='x_earth')
ax1.plot(np.linspace(0, t_span, n_steps), y_positions, label='y_earth')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax1.legend()
ax1.set_title('Position vs Time (Two-Body System)')
ax1.grid()

# Orbit Trace
ax2.plot(x_positions, y_positions, label='Earth')
ax2.plot(0, 0, 'yo', label='Sun')  # Plotting the Sun at the origin
ax2.set_xlabel('X Position (m)')
ax2.set_ylabel('Y Position (m)')
ax2.legend()
ax2.set_title('Orbit Trace (Two-Body System)')
ax2.grid()

plt.tight_layout()
plt.show()
