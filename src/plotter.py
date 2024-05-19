import matplotlib.pyplot as plt


def plot_positions(times, positions, labels, title):
    plt.figure(figsize=(10, 6))
    for i, (pos, label) in enumerate(zip(positions, labels)):
        plt.plot(times, pos, label=label)
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_orbits(positions, labels, title):
    plt.figure(figsize=(10, 10))
    for pos, label in zip(positions, labels):
        plt.plot(pos[0], pos[1], label=label)
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
