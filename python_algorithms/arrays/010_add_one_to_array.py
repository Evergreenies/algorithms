"""
**Challenge:**
You are given a number represented as an array of digits. Each digit in the array 
corresponds to a **single decimal place** in the number. The **most significant 
digit** (highest value) is stored at the **beginning** of the array, following 
**big-endian** notation.
Your task is to **increment** this number by **one**. 

**Example:**
* **Input:** `[1, 2, 3]` (represents the number 123)
* **Output:** `[1, 2, 4]` (represents the number 124)

**Explanation:**
In the input array `[1, 2, 3]`, 1 represents the hundreds digit, 2 represents the 
tens digit, and 3 represents the units digit. Adding one to this number results in 
`124`, represented by the output array `[1, 2, 4]`.

**Clarifications:**
* The input array contains only **non-negative digits** (0-9).
* The digits are stored in **big-endian** format.
* The function should **return** the incremented number represented as an array.
"""


def add_one_to_array(arr: list[int]) -> list[int]:
    carry = 1

    for index in range(len(arr) - 1, -1, -1):
        reminder = (arr[index] + carry) % 10
        carry = (arr[index] + carry) // 10
        arr[index] = reminder

    if carry:
        arr.insert(0, carry)

    return arr


if __name__ == "__main__":
    # assert add_one_to_array([1, 2, 3]) == [1, 2, 4]
    # assert add_one_to_array([]) == [1]
    print(add_one_to_array([9]))
    assert add_one_to_array([9]) == [1, 0]
    assert add_one_to_array([1, 0, 9]) == [1, 1, 0]
    assert add_one_to_array([9, 9, 9]) == [1, 0, 0, 0]
    assert add_one_to_array([9, 8]) == [9, 9]
