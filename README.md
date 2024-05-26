## Simulation of Earth and Jupiter Orbits Around the Sun

### Description

This project simulates the orbital dynamics of Earth and Jupiter around the Sun using numerical methods. It includes two main simulations:
1. **Two-Body Simulation**: Models the orbit of Earth around the Sun, ignoring Jupiter's gravitational influence.
2. **Three-Body Simulation**: Models the orbits of both Earth and Jupiter around the Sun, taking into accounting for their mutual gravitational interactions.

### Files

1. **initial_vals.py**
   - Contains the initial constants and values used for the simulations.
   - Defines the gravitational constant, masses of the Sun, Earth, and Jupiter, and the distances and orbital periods of Earth and Jupiter.
   
2. **two_body.py**
   - Simulates the two-body problem of the Earth orbiting the Sun.
   - Uses Euler's method to update the position and velocity of Earth over time.
   - Plots the position vs. time and the orbit trace of Earth around the Sun.

3. **three_body.py**
   - Simulates the three-body problem including Earth, Jupiter, and the Sun.
   - Uses Euler's method to update the positions and velocities of both Earth and Jupiter over time.
   - Plots the position vs. time for Earth and Jupiter and their orbit traces around the Sun.

### Dependencies

- `numpy`: Used for numerical calculations.
- `matplotlib`: Used for plotting simulation results.

Install these dependencies using pip:
```bash
pip install numpy matplotlib
```

### Usage

#### Running the Two-Body Simulation

1. Ensure that `initial_vals.py` is in the same directory as `two_body.py` and `three_body.py`.
2. Run the `two_body.py` script:
   ```bash
   python two_body.py
   ```
3. The script will generate plots showing Earth's position over time and its orbit around the Sun.

4. Run the `three_body.py` script:
   ```bash
   python three_body.py
   ```
5. The script will generate plots showing the positions of Earth and Jupiter over time and their orbits around the Sun.

### Explanation of Scripts

#### initial_vals.py

Defines constants and initial values:
- Gravitational constant `G`
- Masses of the Sun, Earth, and Jupiter
- Perihelion and aphelion distances of Earth and Jupiter
- Semi-major axes of Earth's and Jupiter's orbits
- Orbital periods of Earth and Jupiter

#### two_body.py

1. Sets initial conditions for Earth's position and velocity.
2. Uses Euler's method to iteratively update Earth's position and velocity over one year.
3. Plots the results: Earth's position vs. time and its orbit trace around the Sun.

#### three_body.py

1. Sets initial conditions for the positions and velocities of Earth and Jupiter.
2. Uses Euler's method to iteratively update the positions and velocities of Earth and Jupiter over one Jupiter year.
3. Plots the results: Positions of Earth and Jupiter vs. time and their orbit traces around the Sun.

### Mathematical and Physical Principles

The simulations rely on:
- **Newton's Laws of Motion**: To calculate accelerations and update positions and velocities.
- **Newton's Law of Universal Gravitation**: To calculate the gravitational forces.
- **Kepler's Laws of Planetary Motion**: To interpret the results.
- **Euler's Method**: For numerical integration to approximate solutions to the differential equations governing the motion.