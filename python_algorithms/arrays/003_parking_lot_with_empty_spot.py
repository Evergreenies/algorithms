"""
**Challenge:**
You are given a parking lot scenario represented by two arrays: `initial_state` and 
`final_state`. Each element in the array represents a car, with a unique identifier 
(e.g., 1, 2, 3, etc.). The number `0` represents an empty parking spot.

**Task:**
1. **Move cars:** You can only move cars **one at a time** by taking a car out of its 
current spot and placing it in the empty spot.
2. **Rearrange:** Your goal is to find the **minimum number of moves** required to 
rearrange the parking lot from the `initial_state` to the `final_state`.
3. **Track changes:** In addition to the minimum number of moves, you also need to 
track and **print the sequence of states** after each move. This sequence should show 
the updated positions of all cars after each car is moved into the empty spot.

**Example:**

* **Initial state:** `[1, 2, 3, 0, 4]` (car 1 is in the empty spot)
* **Final state:** `[0, 3, 2, 1, 4]` (car 3 is in the empty spot)

**Solution:**

- **Move 1:** Swap car 1 with the empty spot, resulting in `[0, 2, 3, 1, 4]`.
- **Move 2:** Swap car 2 with the empty spot, resulting in `[0, 3, 2, 1, 4]`.
- **Move 3:** Swap car 3 with the empty spot, resulting in `[0, 2, 3, 1, 4]`.
- **Move 4:** Swap car 1 with the empty spot again, reaching the final state 
  `[0, 3, 2, 1, 4]`.

**Output:**

```
Initial state: [1, 2, 3, 0, 4]
Final state:   [0, 3, 2, 1, 4]
Steps:         4

Sequence:
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4
```
"""


def rearrange_parking_lot(
    initial_state: list[int], final_state: list[int]
) -> tuple[int, list[list]]:
    steps = 0
    current_state = initial_state[::]
    sequence = []

    while current_state != final_state:
        empty_lot = current_state.index(0)
        if empty_lot != final_state.index(0):
            car_to_move = final_state.index(empty_lot)
            car_position = current_state.index(car_to_move)
            current_state[empty_lot], current_state[car_position] = (
                current_state[car_position],
                current_state[empty_lot],
            )
        else:
            for index in range(len(current_state)):
                if current_state[index] != final_state[index]:
                    current_state[empty_lot], current_state[index] = (
                        current_state[index],
                        current_state[empty_lot],
                    )
                    break
        sequence.append(current_state[::])
        steps += 1
    return steps, sequence


if __name__ == "__main__":
    initial_state = [1, 2, 3, 0, 4]
    final_state = [0, 3, 2, 1, 4]

    steps, sequence = rearrange_parking_lot(initial_state, final_state)
    print(f"{initial_state=}")
    print(f"{final_state=}")
    print(f"{steps=}")
    print(f"{sequence=}")

    assert steps == 4
    assert sequence == [
        [0, 2, 3, 1, 4],
        [2, 0, 3, 1, 4],
        [2, 3, 0, 1, 4],
        [0, 3, 2, 1, 4],
    ]
