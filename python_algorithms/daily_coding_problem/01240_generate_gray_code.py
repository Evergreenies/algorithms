"""
Gray code is a binary code where each successive value differ in only one bit, as well as when 
wrapping around. Gray code is common in hardware so that we don't see temporary spurious values 
during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""


def generate_gray_code(n: int) -> list[str]:
    if n == 0:
        return []

    if n == 1:
        return ["0", "1"]

    prev_gray_code = generate_gray_code(n - 1)
    gray_code = ["0" + code for code in prev_gray_code]

    for index in range(len(prev_gray_code) - 1, -1, -1):
        gray_code.append("1" + prev_gray_code[index])

    return gray_code


if __name__ == "__main__":
    assert generate_gray_code(2) == ["00", "01", "11", "10"]
    assert generate_gray_code(3) == [
        "000",
        "001",
        "011",
        "010",
        "110",
        "111",
        "101",
        "100",
    ]
