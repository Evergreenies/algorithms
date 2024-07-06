"""
The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property:
for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually
results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
"""


def kaprekar_steps(number: int) -> int:
    if not (1000 <= number <= 9999 and len(set(str(number))) >= 2):
        return -1

    seen, steps = set(), 0
    while number != 6174 and number not in seen:
        seen.add(number)
        digits = sorted(str(number))
        desc_num = int("".join(digits[::-1]))
        number = desc_num - int("".join(digits))
        steps += 1

    return steps if number == 6174 else -1


assert kaprekar_steps(1234) == 3
assert kaprekar_steps(1111) == -1
