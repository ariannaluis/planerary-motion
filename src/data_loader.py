"""
Functions to load masses and orbital parameters from JSON files.
"""

import os
import json


def load_masses():
    """
    Load masses of bodies from a JSON file
    :return:    (dict) dictionary containing the masses of the sun, the planet,
                and Jupiter
    """
    file_path = os.path.join(os.path.dirname(__file__), '../data/masses.json')

    try:
        with open(file_path, "r") as file:
            data = ""
            for chunk in iter(lambda: file.read(4096), ""):
                data += chunk
            return json.loads(data)
    except Exception as e:
        print(f"Error loading masses: {e}")
        return None


def load_orbital_params(file_path="data/orbital_params.json"):
    """
    Load orbital parameters of bodies from a JSON file
    :param      file_path: (str) path vto the JSON file that contains the
                parameters
    :return:    (dict) dictionary containing the orbital parameters for the planet
                and Jupiter
    """
    file_path = os.path.join(os.path.dirname(__file__), '../data/orbital_params.json')

    try:
        with open(file_path, "r") as file:
            data = ""
            for chunk in iter(lambda: file.read(4096), ""):
                data += chunk
            return json.loads(data)
    except Exception as e:
        print(f"Error loading orbital parameters: {e}")
        return None
