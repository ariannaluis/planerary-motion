"""
Functions to plot the results of the simulations
"""

import matplotlib.pyplot as plt


def plot_positions(times, positions, labels, title):
    """
    Plot the positions of celestial bodies as a function of time
    :param times:       (array)             array of time points
    :param positions:   (list of arrays)    list of position arrays
    :param labels:      (list of str)       labels for each position array
    :param title:       (str)               title of the plot
    """
    # new figure for plot
    plt.figure(figsize=(10, 6))

    # plot each position array with its label
    for i, (pos, label) in enumerate(zip(positions, labels)):
        plt.plot(times, pos, label=label)

    # set plot labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title(title)
    plt.legend()
    plt.grid(True)

    # display the plot
    # plt.show()


def plot_orbits(positions, labels, title):
    """
    Plot the orbits of celestial bodies
    :param positions:   (list of list of arrays) list of position arrays for each body
    :param labels:      (list of str)            labels for each orbit
    :param title:       (str)                    title of the plot
    """
    # new figure for plot
    plt.figure(figsize=(10, 10))

    # plot the orbit of each body
    for pos, label in zip(positions, labels):
        plt.plot(pos[0], pos[1], label=label)

    # set plot labels and title
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')

    # display the plot
    # plt.show()


def save_plot(file_path):
    """
    Save the current plot to a file
    :param file_path: (str) path to save the plot file
    """
    plt.savefig(file_path)
    plt.close()
