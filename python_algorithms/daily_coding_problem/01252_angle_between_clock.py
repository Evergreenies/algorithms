"""
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
"""


def angle_between_hands(time_string: str) -> int:
    hours, minutes = map(int, time_string.split(":"))
    if hours >= 0 and minutes >= 0:
        angle = ((hours % 12) * 30) - (minutes * 0.5)
        if (hours % 12) == 0:
            return round(abs(angle))
        return round(angle)

    return -1


if __name__ == "__main__":
    assert angle_between_hands("03:00") == 90
    assert angle_between_hands("12:00") == 0
    assert angle_between_hands("12:30") == 15
