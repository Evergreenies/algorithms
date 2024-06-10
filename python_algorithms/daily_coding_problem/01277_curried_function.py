"""
Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:

add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 - 2 + 3 -> 2

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
"""


class AddSubtract:
    sign: bool = True

    def __init__(self, value):
        self.value = value

    def __call__(self, num):
        AddSubtract.sign = not AddSubtract.sign
        _sign = 1 if AddSubtract.sign else -1

        self.value += num * _sign
        return AddSubtract(self.value)

    def __repr__(self):
        return str(self.value)


def add_subtract(num):
    AddSubtract.sign = True if num > 0 else False
    return AddSubtract(num)


print(add_subtract(7))  # Output: 7
print(add_subtract(1)(2)(3))  # Output: 2
print(add_subtract(-5)(10)(3)(9))  # Output: 11
