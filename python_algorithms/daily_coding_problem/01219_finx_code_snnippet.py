"""
What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

from typing import Callable


functions = []


def closure(item: int) -> Callable:
    return lambda: item


for i in range(10):
    functions.append(closure(i))

for f in functions:
    print(f())
