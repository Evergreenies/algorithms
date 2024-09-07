"""
Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.
"""

import random
from typing import Iterable


def pick_element_from_stream(stream: Iterable) -> int | None:
    reservoir = None
    for index, item in enumerate(stream, 1):
        if index == 1:
            reservoir = item
        else:
            if random.randint(1, index) == 1:
                reservoir = item

    return reservoir


print(pick_element_from_stream(iter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])))
