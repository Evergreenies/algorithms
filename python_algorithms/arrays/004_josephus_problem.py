"""
**Challenge:** 
Imagine a group of people sitting in a circle, numbered consecutively from 1 to N. You want to remove people 
from the circle one by one, following a specific rule. 

**Rule:**
1. **Start at any person:** You can begin by pointing to any person in the circle.
2. **Skip two, remove one:** Starting from the chosen person, skip the next two people and remove the third 
person from the circle.
3. **Continue the process:** Repeat step 2, starting from the person **immediately** after the one you just removed.
4. **Print remaining numbers:** Print the numbers of the remaining people in the order they are removed, 
eventually printing all people and emptying the circle.

**Example:**
* **Input:** Consider a circle of 9 people numbered 1, 2, 3, 4, 5, 6, 7, 8, and 9.
* **Output:** The order of people removed, and consequently printed, would be: 3 6 9 4 8 5 2 7 1.
"""


from typing import Any


def remove_every_nth_circular(peoples: str | list[Any], skip: int) -> str:
    peoples = list(map(int, peoples)) if isinstance(peoples, str) else peoples
    current_index, skip = 0, skip - 1
    removed_sequence = ""

    while peoples:
        removed_index = (current_index + skip) % len(peoples)
        removed_person = peoples.pop(removed_index)
        removed_sequence += str(removed_person)
        current_index = removed_index
    return removed_sequence


if __name__ == "__main__":
    assert remove_every_nth_circular("123456789", 3) == "369485271"
    assert (
        remove_every_nth_circular(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3)
        == "369485271"
    )
