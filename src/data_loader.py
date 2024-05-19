import json


def load_masses(file_path="data/masses.json"):
    with open(file_path, "r") as file:
        return json.load(file)


def load_orbital_params(file_path="data/orbital_params.json"):
    with open(file_path, "r") as file:
        return json.load(file)
