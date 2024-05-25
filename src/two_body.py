import data.initial_vals as vals
import numpy as np
import matplotlib.pyplot as plt

# initial conditions for earth
x_earth = vals.earth_perihelion    # initial position in x, meters
y_earth = 0.0               #initial position in y, meters
vx_earth = 0.0              # initial velocity in x, meters/second
vy_earth = np.sqrt(vals.G * vals.m_sun * ((2/vals.earth_perihelion) - (1 / vals.earth_semi_major)))

# simulation parameters
t_span = 31558149.8         # one year in seconds
dt = 60 * 60                 # one day in seconds
n_steps = int(t_span / dt)

# arrays to store the positions and velocities
x_positions = np.zeros(n_steps)
y_positions = np.zeros(n_steps)
vx = vx_earth
vy = vy_earth
x = x_earth
y = y_earth

# euler's method for integration
for i in range(n_steps):
    r = np.sqrt(x**2 + y**2)
    ax = -vals.G * vals.m_sun * x / r**3
    ay = -vals.G * vals.m_sun * y / r**3
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    x_positions[i] = x
    y_positions[i] = y

# plot results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# position vs time
ax1.plot(np.linspace(0, t_span, n_steps), x_positions, label='x_earth')
ax1.plot(np.linspace(0, t_span, n_steps), y_positions, label='y_earth')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax1.legend()
ax1.set_title('Position vs Time (Two-Body System)')
ax1.grid()

# orbit trace
ax2.plot(x_positions, y_positions, label='Earth')
ax2.plot(0, 0, 'yo', label='Sun')  # Plotting the Sun at the origin
ax2.set_xlabel('X Position (m)')
ax2.set_ylabel('Y Position (m)')
ax2.legend()
ax2.set_title('Orbit Trace (Two-Body System)')
ax2.grid()

plt.tight_layout()
plt.show()
