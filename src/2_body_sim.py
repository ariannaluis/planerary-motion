import numpy as np
import matplotlib.pyplot as plt
from data.constants import G, M_SUN, M_EARTH, PER_EARTH, SEMIMAJOR_EARTH
from src.formulas import gravitational_force, acceleration, update_position, update_velocity, vis_visa


# define sim parameters
def earth_simulation(years, dt):
    seconds = years * 365 * 24 * 60 * 60    # years to seconds
    num_steps = int(seconds/dt)

    # init np arrays to store positions and velocities
    earth_positions = np.zeros((num_steps, 2))
    earth_velocities = np.zeros((num_steps, 2))

    # init conditions (earth at perihelion)
    earth_positions[0] = np.array([PER_EARTH, 0])   # x=perihelion, y=0
    earth_velocities[0] = np.array([0, vis_visa(M_SUN, PER_EARTH,
                                                SEMIMAJOR_EARTH)])

    # simulation loop
    for i in range(1, num_steps):
        # calculate acceleration
        force_earth_sun = gravitational_force(M_EARTH, M_SUN, earth_positions[i-1],
                                              np.array([0, 0]))
        accel_earth = acceleration(force_earth_sun, M_EARTH)

        # update velocity and position
        earth_velocities[i] = update_velocity(earth_velocities[i-1], accel_earth, dt)
        earth_positions[i] = update_position(earth_positions[i-1], earth_velocities[i], dt)

    return earth_positions


def plot_orbit(positions, duration):
    time = np.linspace(0, duration, num=positions.shape[0])     # time array

    # xEarth vs t and yEarth vs t
    plt.plot(time, positions[:, 0], label='xEarth')
    plt.plot(time, positions[:, 1], label='yEarth')
    plt.xlabel('Time (years)')
    plt.ylabel('Position (m)')
    plt.legend()
    plt.title('Motion of Earth over 3 Earth years')
    plt.show()

    # trace of earth’s orbit
    plt.plot(positions[:, 0], positions[:, 1], label="Earth's Orbit")
    plt.scatter(0, 0, color='yellow', label='Sun')
    plt.xlabel('x position (m)')
    plt.ylabel('y position (m)')
    plt.legend()
    plt.title("Trace of Earth's Orbit over 3 Earth years")
    plt.grid(True)
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    # define simulation parameters
    duration_years = 3
    timestep = 60 * 60    # delta t for 1 hour

    # run simulation
    earth_pos = earth_simulation(duration_years, timestep)

    # plot simulation
    plot_orbit(earth_pos, duration_years)
