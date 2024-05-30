"""
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
For example, given [10, 7, 76, 415], you should return 77641510.
"""


def first_digit(num: int) -> int:
    last_rem = num
    while num > 0:
        num //= 10

        if num > 0:
            last_rem = num

    return last_rem


def bubble_sort(arr: list[int]) -> list[int]:
    swapped = True
    while swapped:
        swapped = False

        for index in range(len(arr) - 1):
            if first_digit(arr[index]) < first_digit(arr[index + 1]):
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True

        if not swapped:
            break

    return arr


def largest_number(arr: list[int]) -> str:
    arr = bubble_sort(arr)
    return "".join(str(num) for num in arr)


if __name__ == "__main__":
    assert largest_number([0, 0]) == "00"
    assert largest_number([10, 7, 76, 415]) == "77641510"
