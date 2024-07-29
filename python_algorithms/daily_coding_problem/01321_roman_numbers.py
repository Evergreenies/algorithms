"""
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
"""


def roman_to_deciman(roman: str) -> int:
    romans = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    total, length = 0, len(roman)
    for index in range(length):
        if index < length - 1 and romans.get(roman[index], 0) < romans.get(
            roman[index + 1], 0
        ):
            total -= romans.get(roman[index], 0)
        else:
            total += romans.get(roman[index], 0)

    return total


print(roman_to_deciman("XIV"))
print(roman_to_deciman("MCMXCIV"))
