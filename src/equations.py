import numpy as np

G = 6.67430e-11  # gravitational constant


def gravitational_force(m1, m2, r):
    return G * m1 * m2 / np.linalg.norm(r) ** 3 * r


def differential_equations(t, state, masses):
    if len(masses) == 2:  # Two-body case
        x1, y1, vx1, vy1, x2, y2, vx2, vy2 = state
        m1, m2 = masses
        r12 = np.array([x2 - x1, y2 - y1])

        a1 = gravitational_force(m2, m1, -r12) / m1
        a2 = gravitational_force(m1, m2, r12) / m2

        return [vx1, vy1, *a1, vx2, vy2, *a2]
    elif len(masses) == 3:  # Three-body case
        x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = state
        m1, m2, m3 = masses
        r12 = np.array([x2 - x1, y2 - y1])
        r13 = np.array([x3 - x1, y3 - y1])
        r23 = np.array([x3 - x2, y3 - y2])

        a1 = gravitational_force(m2, m1, -r12) / m1 + gravitational_force(m3, m1, -r13) / m1
        a2 = gravitational_force(m1, m2, r12) / m2 + gravitational_force(m3, m2, -r23) / m2
        a3 = gravitational_force(m1, m3, r13) / m3 + gravitational_force(m2, m3, r23) / m3

        return [vx1, vy1, *a1, vx2, vy2, *a2, vx3, vy3, *a3]


def difference_equations(state, masses, dt):
    if len(masses) == 2:  # Two-body case
        x1, y1, vx1, vy1, x2, y2, vx2, vy2 = state
        m1, m2 = masses
        r12 = np.array([x2 - x1, y2 - y1])

        a1 = gravitational_force(m2, m1, -r12) / m1
        a2 = gravitational_force(m1, m2, r12) / m2

        vx1_new = vx1 + a1[0] * dt
        vy1_new = vy1 + a1[1] * dt
        vx2_new = vx2 + a2[0] * dt
        vy2_new = vy2 + a2[1] * dt

        x1_new = x1 + vx1_new * dt
        y1_new = y1 + vy1_new * dt
        x2_new = x2 + vx2_new * dt
        y2_new = y2 + vy2_new * dt

        return [x1_new, y1_new, vx1_new, vy1_new, x2_new, y2_new, vx2_new, vy2_new]
    elif len(masses) == 3:  # Three-body case
        x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = state
        m1, m2, m3 = masses
        r12 = np.array([x2 - x1, y2 - y1])
        r13 = np.array([x3 - x1, y3 - y1])
        r23 = np.array([x3 - x2, y3 - y2])

        a1 = gravitational_force(m2, m1, -r12) / m1 + gravitational_force(m3, m1, -r13) / m1
        a2 = gravitational_force(m1, m2, r12) / m2 + gravitational_force(m3, m2, -r23) / m2
        a3 = gravitational_force(m1, m3, r13) / m3 + gravitational_force(m2, m3, r23) / m3

        vx1_new = vx1 + a1[0] * dt
        vy1_new = vy1 + a1[1] * dt
        vx2_new = vx2 + a2[0] * dt
        vy2_new = vy2 + a2[1] * dt
        vx3_new = vx3 + a3[0] * dt
        vy3_new = vy3 + a3[1] * dt

        x1_new = x1 + vx1_new * dt
        y1_new = y1 + vy1_new * dt
        x2_new = x2 + vx2_new * dt
        y2_new = y2 + vy2_new * dt
        x3_new = x3 + vx3_new * dt
        y3_new = y3 + vy3_new * dt

        return [x1_new, y1_new, vx1_new, vy1_new, x2_new, y2_new, vx2_new, vy2_new, x3_new, y3_new, vx3_new, vy3_new]
