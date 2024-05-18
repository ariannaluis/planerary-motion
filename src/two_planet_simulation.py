"""
Simulation for a single terrestrial object and Jupiter orbiting the Sun
"""

import json

with open('../data/planetary_data.json', 'r') as f:
    data = json.load(f)

G = data['constants']['G']

if __name__ == "__main__":
    # load data from planetary_data.json
    # compute initial conditions for earth and jupiter using utils.py
    # run simulation for 36 years
    # store positions
    # plot results
    holder = None
