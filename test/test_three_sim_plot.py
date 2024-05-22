import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  # gravitational constant, m^3 kg^-1 s^-2
m_sun = 1.989e30  # mass of the Sun, kg
m_earth = 5.972e24  # mass of the Earth, kg
m_jupiter = 1.898e27  # mass of Jupiter, kg

x_earth = 147095000000.0  # initial position in x, meters
y_earth = 0.0  # initial position in y, meters
vx_earth = 0.0  # initial velocity in x, meters/second
vy_earth = 30286.4027  # initial velocity in y, meters/second

x_jupiter = 778500000000.0  # initial position in x, meters
y_jupiter = 0.0  # initial position in y, meters
vx_jupiter = 0.0  # initial velocity in x, meters/second
vy_jupiter = 13070.0  # initial velocity in y, meters/second

t_span = 31558118.4 * 11.86  # 11.86 years in seconds (one Jupiter year)
dt = 86400  # one day in seconds
n_steps = int(t_span / dt)

# arrays to store the positions
x_positions_earth = np.zeros(n_steps)
y_positions_earth = np.zeros(n_steps)
x_positions_jupiter = np.zeros(n_steps)
y_positions_jupiter = np.zeros(n_steps)

# initial values
vx_earth_current = vx_earth
vy_earth_current = vy_earth
x_earth_current = x_earth
y_earth_current = y_earth

vx_jupiter_current = vx_jupiter
vy_jupiter_current = vy_jupiter
x_jupiter_current = x_jupiter
y_jupiter_current = y_jupiter

# euler's method
for i in range(n_steps):
    # update earth
    r_earth = np.sqrt(x_earth_current**2 + y_earth_current**2)
    ax_earth = -G * m_sun * x_earth_current / r_earth**3
    ay_earth = -G * m_sun * y_earth_current / r_earth**3
    vx_earth_current += ax_earth * dt
    vy_earth_current += ay_earth * dt
    x_earth_current += vx_earth_current * dt
    y_earth_current += vy_earth_current * dt
    x_positions_earth[i] = x_earth_current
    y_positions_earth[i] = y_earth_current

    # update jupiter's position and velocity
    r_jupiter = np.sqrt(x_jupiter_current**2 + y_jupiter_current**2)
    ax_jupiter = -G * m_sun * x_jupiter_current / r_jupiter**3
    ay_jupiter = -G * m_sun * y_jupiter_current / r_jupiter**3
    vx_jupiter_current += ax_jupiter * dt
    vy_jupiter_current += ay_jupiter * dt
    x_jupiter_current += vx_jupiter_current * dt
    y_jupiter_current += vy_jupiter_current * dt
    x_positions_jupiter[i] = x_jupiter_current
    y_positions_jupiter[i] = y_jupiter_current

# plot results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# position vs time for earth
ax1.plot(np.linspace(0, t_span, n_steps), x_positions_earth, label='x_earth')
ax1.plot(np.linspace(0, t_span, n_steps), y_positions_earth, label='y_earth')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax1.legend()
ax1.set_title('Position vs Time for Earth')
ax1.grid()

# position vs time for jupiter
ax1.plot(np.linspace(0, t_span, n_steps), x_positions_jupiter, label='x_jupiter', linestyle='--')
ax1.plot(np.linspace(0, t_span, n_steps), y_positions_jupiter, label='y_jupiter', linestyle='--')
ax1.legend()

# orbit trace
ax2.plot(x_positions_earth, y_positions_earth, label='Earth')
ax2.plot(x_positions_jupiter, y_positions_jupiter, label='Jupiter', linestyle='--')
ax2.plot(0, 0, 'yo', label='Sun')  # Plotting the Sun at the origin
ax2.set_xlabel('X Position (m)')
ax2.set_ylabel('Y Position (m)')
ax2.legend()
ax2.set_title('Orbit Trace')
ax2.grid()

plt.tight_layout()
plt.show()
