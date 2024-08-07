"""
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""


def spreadsheet_columns_numbering(column_number: int) -> str:
    result = ""
    while column_number > 0:
        column_number -= 1
        remainder = column_number % 26
        result = chr(ord("A") + remainder) + result
        column_number //= 26

    return result


print(spreadsheet_columns_numbering(28))
print(spreadsheet_columns_numbering(1))
print(spreadsheet_columns_numbering(27))
