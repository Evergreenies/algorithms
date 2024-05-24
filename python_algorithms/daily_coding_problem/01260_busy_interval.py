"""
You are given a list of data entries that represent entries and exits of groups of people into a building. 
An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it 
as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, 
i.e. with 0 people inside.
"""

from collections import deque
from typing import Any


def fin_busiest_period(data: list[Any]) -> tuple[int | None, int | None]:
    data.sort(key=lambda x: x["timestamp"])
    current_count, max_count = 0, 0
    start_time, end_time = None, None
    people_in_building = deque()

    for entry in data:
        if entry["type"] == "enter":
            people_in_building.append(entry["timestamp"])
            current_count += entry["count"]
        else:
            people_in_building.popleft()
            current_count -= entry["count"]

        if current_count > max_count:
            max_count = current_count
            start_time = people_in_building[0]

    if start_time is not None:
        end_time = (
            data[-1]["timestamp"]
            if data[-1]["timestamp"] == "exit"
            else data[-1]["timestamp"] - 1
        )

    return start_time, end_time


if __name__ == "__main__":
    data = [
        {"timestamp": 1526579928, "count": 3, "type": "enter"},
        {"timestamp": 1526580023, "count": 1, "type": "enter"},
        {"timestamp": 1526580382, "count": 2, "type": "exit"},
        {"timestamp": 1526580423, "count": 4, "type": "enter"},
        {"timestamp": 1526580542, "count": 1, "type": "exit"},
    ]
    print(fin_busiest_period(data.copy()))
