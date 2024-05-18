import time

import numpy as np
import matplotlib.pyplot as plt
from data.constants import G, M_SUN, M_EARTH, PER_EARTH, SEMIMAJOR_EARTH
from src.formulas import gravitational_force, acceleration, update_position, update_velocity, vis_visa
from log import SimulationLogger


# define sim parameters
def earth_simulation(years, dt, logger):
    progress_interval = 1000
    seconds = years * 365 * 24 * 60 * 60  # years to seconds
    num_steps = int(seconds / dt)

    # init np arrays to store positions and velocities
    earth_positions = np.zeros((num_steps, 2))
    earth_velocities = np.zeros((num_steps, 2))

    # init conditions (earth at perihelion)
    earth_positions[0] = np.array([PER_EARTH, 0])  # x=perihelion, y=0
    earth_velocities[0] = np.array([0, vis_visa(M_SUN, PER_EARTH,
                                                SEMIMAJOR_EARTH)])

    # simulation loop
    for i in range(1, num_steps):
        # calculate acceleration
        force_earth_sun = gravitational_force(M_EARTH, M_SUN, earth_positions[i - 1],
                                              np.array([0, 0]))
        accel_earth = acceleration(force_earth_sun, M_EARTH)

        # update velocity and position
        earth_velocities[i] = update_velocity(earth_velocities[i - 1], accel_earth, dt)
        earth_positions[i] = update_position(earth_positions[i - 1], earth_velocities[i], dt)

        if i % progress_interval == 0:
            logger.log_progress(i, num_steps)

    logger.log_progress(num_steps, num_steps)
    logger.log_blank_line()

    return earth_positions


def plot_orbit(positions, duration):
    time_arr = np.linspace(0, duration, num=positions.shape[0])  # time array

    # xEarth vs t, yEarth vs t
    plt.plot(time_arr, positions[:, 0], label='xEarth')
    plt.plot(time_arr, positions[:, 1], label='yEarth')
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
    logger = SimulationLogger(log_dir='../results/logs')

    # define and log simulation parameters
    duration_years = 3
    timestep = 60 * 60  # delta t for 1 hour

    params = {'duration_years': duration_years,
              'dt': timestep}
    logger.log_params(params)

    # run simulation
    start_time = time.time()
    earth_pos = earth_simulation(duration_years, timestep, logger)
    end_time = time.time()

    runtime = end_time - start_time
    logger.log_runtime(runtime)

    # plot simulation
    plot_orbit(earth_pos, duration_years)
