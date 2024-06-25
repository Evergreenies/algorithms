"""
Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are
printed out diagonally from top left to bottom right until reaching the kth line, then back up to
top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
"""


def convert(string: str, num_rows: int):
    if num_rows == 1:
        return string

    rows = ["" for _ in range(num_rows)]
    curr_row, going_down = 0, False

    for char in string:
        rows[curr_row] += char

        if curr_row == 0 or curr_row == num_rows - 1:
            going_down = not going_down

        curr_row += 1 if going_down else -1

    return "".join(rows)


print(convert("thisisazigzag", 4))
