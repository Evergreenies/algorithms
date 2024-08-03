"""
`reduce` (also known as fold) is a function that takes in an array, a combining function, and an initial
value and builds up a result by calling the combining function on each element of the array, left to right.

For example, we can write sum() in terms of reduce:

def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

This should call add on the initial value with the first element of the array, and then the result of that
with the second element of the array, and so on until we reach the end, when we return the sum of the array.

Implement your own version of reduce.
"""

from typing import Callable


def reduce(arr: list, func: Callable, initial: int) -> int | float:
    result = initial
    for ele in arr:
        result = func(result, ele)

    return result


def add(a: int, b: int) -> int:
    return a + b


def mult(a: int, b: int) -> int:
    return a * b


def accumulate(arr: list, func: Callable = add, initial: int = 0) -> int | float:
    return reduce(arr, func, initial)


print(accumulate([1, 2, 3, 4, 5, 6]))
print(accumulate([1, 2, 3, 4, 5, 6], mult, 1))
