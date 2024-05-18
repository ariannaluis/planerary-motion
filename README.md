# Planetary Motion Simulation

## Overview
This project simulates the motion of celestial bodies in a simplified two-body system using Newton's laws of motion and gravitation. Specifically, it focuses on modeling the motion of the Earth in the presence of gravitational forces exerted by the Sun and other planets, such as Jupiter.

## Theory
- **Newton's Second Law:** Describes the motion of an object in a 2D plane under the influence of external forces. For a constant mass object like a planet, the acceleration in the x and y directions is determined by the net force acting on it divided by its mass. 
- **Newton's Law of Universal Gravitation:** Defines the gravitational force between two spherically symmetric bodies. The force between two bodies is inversely proportional to the square of the distance between their centers and directly proportional to the product of their masses.
- **Kepler's Law:**

## Project Goals
1. **Data Collection:**
2. **Equations of Motion:**
3. **Simulation Setup:**
4. **Simulation and Visualization:**
5. **Extended Simulation:**

## Requirements
- Python 3.10
- Numpy
- Matplotlib

## Installation
1. Clone the repository:
`git clone https://github.com/ariannaluis/planetary-motion.git`
2. Navigate to the project directory: `cd planetary-motion
`
3. Install dependencies `pip install -r requirements.txt
`

## Usage
1. Run the simulation script: `python src/2_body_sim.py
`
2. Adjust simulation parameters in the script file as needed.
3. View simulation results in the `results/plots` directory.
4. Check the simulation log file in the `results/logs` directory for details.

## Configuration
- Modify simulation parameters such as duration and timestep in `2_body_sim.py`. 
- Customize logging behavior in `log.py`.