"""
**Challenge:**
You are given an array of numbers, and you want to **filter** it based on certain conditions. 
This filtering can be used to:

1. **Limit values based on a range:** You can keep only elements from the array that are within 
a specific range.
2. **Extract specific values:** You can keep only elements that are above a certain minimum value 
or below a certain maximum value.

This problem introduces a function called `limit` that takes three arguments:
* **array:** The original array of numbers.
* **min_value:** The minimum value threshold (optional, can be `None` for no lower bound).
* **max_value:** The maximum value threshold (optional, can be `None` for no upper bound).

The `limit` function should return a new array containing only the elements from the original array 
that satisfy the following conditions:
* If both `min_value` and `max_value` are provided, only elements **greater than** `min_value` and 
**less than** `max_value` are included in the result.
* If only `min_value` is provided (and `max_value` is `None`), only elements **greater than** `min_value` 
are included.
* If only `max_value` is provided (and `min_value` is `None`), only elements **less than** `max_value` 
are included.
* If both `min_value` and `max_value` are `None` (or the string `"unlimit"` is provided for either), that 
specific limit is considered "unbounded," and elements are not filtered based on that limit.

**Example:**
* **Input:** `limit([1, 2, 3, 4, 5], None, 3)`
* **Output:** `[1, 2, 3]` (Elements less than or equal to 3 are excluded)
* **Input:** `limit([1, 2, 3, 4, 5], 2, None)`
* **Output:** `[3, 4]` (Elements less than 2 are excluded)

**Complexity:**
The function should have a time complexity of O(n), meaning the execution time grows linearly with the size of the input array.
"""


def limit_array(
    arr: list[int], min_limit: int | None = None, max_limit: int | None = None
) -> list[int]:
    if len(arr) == 0:
        return arr

    min_limit = min_limit if min_limit is not None else min(arr)
    max_limit = max_limit if max_limit is not None else max(arr)

    return list(filter(lambda element: (min_limit <= element <= max_limit), arr))


if __name__ == "__main__":
    assert limit_array([1, 2, 3, 4, 5], min_limit=None, max_limit=3) == [1, 2, 3]
    assert limit_array([], None, 3) == []
    assert limit_array([1], 0, 0) == []
    assert limit_array([1, 1], 1, 1) == [1, 1]
    assert limit_array([1, 1, 2], 1, 1) == [1, 1]
    assert limit_array([1, 1, 2], 1, 0) == []
