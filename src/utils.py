"""
Utility functions for common calculations such as conversions and orbital parameters
"""


def years_to_seconds(years):
    """
    Converts years to seconds
    :param years: (int) time in years
    :return: (int) time in seconds
    """
    return 0


def gravitational_force(M1, M2, r):
    """
    Calculates the gravitational force between two masses
    :param M1: (float) mass of the first body
    :param M2: (float) mass of the second body
    :param r: (float) distance between the two bodies
    :return: (float) gravitational force
    """
    return 0


def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points in 2D space
    :param x1: (float) x-coordinate of the first point
    :param y1: (float) y-coordinate of the first point
    :param x2: (float) x-coordinate of the second point
    :param y2: (float) y-coordinate of the second point
    :return: (float) distance between the points
    """
    return 0


def vector_components(x1, y1, x2, y2):
    """
    Calculate vector components from point 1 to point 2
    :param x1: (float) x-coordinate of the first point
    :param y1: (float) y-coordinate of the first point
    :param x2: (float) x-coordinate of the second point
    :param y2: (float) y-coordinate of the second point
    :return: (tuple) vector components (dx, dy)
    """
    return 0


def magnitude(dx, dy):
    """
    Calculate the magnitude of a vector given its components
    :param dx: (float) dx vector component
    :param dy: (float) dy vector component
    :return: (float) magnitude of the vector
    """
    return 0


def semi_major_axis(perihelion, aphelion):
    """
    Calculates the semi-major axis of an elliptical orbit, which is the average
    of the perihelion and aphelion distances
    :param perihelion: (float) closest distance of the orbit to the sun
    :param aphelion: (float) furthest distance of the orbit to the sun
    :return: (float) semi-major axis
    """
    return 0


def semi_minor_axis(semi_major, perihelion):
    """
    Calculates the semi-minor axis of an elliptical orbit using the semi-major
    axis and aphelion distances
    :param semi_major: (float) semi-major axis of the orbit
    :param perihelion:(float) closest distance of the orbit to the sun
    :return: (float) semi-minor axis
    """
    return 0


def orbital_area(semi_major, semi_minor):
    """
    Calculates the area of an elliptical orbit
    :param semi_major: (float) semi-major axis of the orbit
    :param semi_minor: (float) semi-minor axis of the orbit
    :return: (float) area of the orbit
    """
    return 0


def perihelion_speed(semi_major, orbital_period, area):
    """
    Calculates the speed of the planet at perihelion using Kepler's Second Law
    :param semi_major: (float) semi-major axis of the orbit
    :param orbital_period: (float) time to complete one orbit
    :param area: (float) area of the orbit
    :return: (float) speed at perihelion
    """
    return 0
