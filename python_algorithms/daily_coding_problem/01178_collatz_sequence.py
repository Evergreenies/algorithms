"""
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

- if n is even, the next number in the sequence is n / 2
- if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""


def collatz_sequence(num: int) -> int:
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (3 * num) + 1
        steps += 1

    return steps


def find_longest_sequence(upper_bound: int) -> tuple[int, int]:
    longest_num = 1
    longest_length = 0

    for num in range(2, upper_bound + 1):
        current_length = collatz_sequence(num)
        if current_length > longest_length:
            longest_num = num
            longest_length = current_length

    return longest_num, longest_length


if __name__ == "__main__":
    print(find_longest_sequence(1000000))
