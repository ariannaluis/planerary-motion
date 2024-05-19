"""
Functions to load masses and orbital parameters from JSON files.
"""

import json


def load_masses(file_path="data/masses.json"):
    """
    Load masses of bodies from a JSON file
    :param      file_path: (str) path to the JSON file that contains the masses
    :return:    (dict) dictionary containing the masses of the sun, the planet,
                and Jupiter
    """
    with open(file_path, "r") as file:
        return json.load(file)


def load_orbital_params(file_path="data/orbital_params.json"):
    """
    Load orbital parameters of bodies from a JSON file
    :param      file_path: (str) path vto the JSON file that contains the
                parameters
    :return:    (dict) dictionary containing the orbital parameters for the planet
                and Jupiter
    """
    with open(file_path, "r") as file:
        return json.load(file)
