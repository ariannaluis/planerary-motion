import constants as c
from src.formulas import vis_visa

# initial x position at perihelion (m)
X0_EARTH = c.PER_EARTH
X0_JUPITER = c.PER_JUPITER

# initial y position (m)
Y0_EARTH = 0
Y0_JUPITER = 0

# initial x velocity (m/s)
VX0_EARTH = 0
VX0_JUPITER = 0

# initial y velocity at perihelion (m/s)
VY0_EARTH = vis_visa(c.M_SUN, c.PER_EARTH, c.SEMIMAJOR_EARTH)
VY0_JUPITER = vis_visa(c.M_SUN, c.PER_JUPITER, c.SEMIMAJOR_JUPITER)
