"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random


def estimate_pi(simulations: int) -> float:
    circle_points = 0
    square_points = simulations

    for _ in range(simulations):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if ((x**2) + (y**2)) <= 1:
            circle_points += 1

    pi_estimate = (circle_points / square_points) * 4
    return round(pi_estimate, 3)


if __name__ == "__main__":
    print(estimate_pi(1000000))
