# Happy number

def is_happy(num: int) -> bool:
    visited = set()
    while num != 1 and not (num in visited):
        visited.add(num)
        num = get_sum_of_digits(num)

    return num == 1


def get_sum_of_digits(num: int) -> int:
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num = num // 10

    return _sum


print(is_happy(19))
print(is_happy(20))
print(is_happy(21))
print(is_happy(22))
