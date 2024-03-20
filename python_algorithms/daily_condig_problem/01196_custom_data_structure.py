"""
Create a data structure that performs all the following operations in O(1) time:

plus: Add a key with value 1. If the key already exists, increment its value by one.
minus: Decrement the value of a key. If the key's value is currently 1, remove it.
get_max: Return a key with the highest value.
get_min: Return a key with the lowest value.
"""
import math

from collections import defaultdict
from typing import Any


class CountMap:
    def __init__(self) -> None:
        self.count_map = defaultdict(int)
        self.max_key, self.min_key = None, None

    def plus(self, key: Any) -> None:
        self.count_map[key] += 1

        if self.count_map[key] < self.count_map.get(self.max_key, math.inf):
            self.min_key = key

        if self.count_map[key] > self.count_map.get(self.max_key, -math.inf):
            self.max_key = key

    def minus(self, key: Any) -> None:
        if key not in self.count_map:
            return

        self.count_map[key] -= 1
        if self.count_map[key] == 0:
            del self.count_map[key]

        if key == self.min_key:
            min_key, min_value = (
                None,
                self.count_map.get(self.min_key, math.inf),
            )
            for key, value in self.count_map.items():
                if value <= min_value:
                    min_key, min_value = key, value
                    break

            self.min_key = min_key

        if key == self.max_key:
            max_key, max_value = (
                None,
                self.count_map.get(self.max_key, -math.inf),
            )
            for key, value in self.count_map.items():
                if value >= max_value:
                    max_key, max_value = key, value

            self.max_key = max_key

    def get_max(self) -> Any | None:
        return self.max_key

    def get_min(self) -> Any | None:
        return self.min_key


if __name__ == "__main__":
    count_map = CountMap()
    count_map.minus("a")
    assert count_map.get_max() is None
    assert count_map.get_min() is None

    count_map.plus("a")
    assert count_map.get_max() == "a"
    assert count_map.get_min() == "a"

    count_map.plus("a")
    assert count_map.get_max() == "a"
    assert count_map.get_min() == "a"

    count_map.plus("b")
    assert count_map.get_max() == "a"
    assert count_map.get_min() == "b"

    count_map.minus("b")
    assert count_map.get_max() == "a"
    assert count_map.get_min() == "a"

    count_map.minus("b")
    assert count_map.get_max() == "a"
    assert count_map.get_min() == "a"

    count_map.minus("a")
    assert count_map.get_max() == "a"
    assert count_map.get_min() == "a"

    count_map.minus("a")
    assert count_map.get_max() is None
    assert count_map.get_min() is None
