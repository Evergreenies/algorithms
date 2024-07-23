"""
The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term
visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""


def look_and_say(nth: int) -> str:
    if nth == 1:
        return "1"

    prev_term = "1"
    for _ in range(2, nth + 1):
        next_term, count = "", 1

        for index in range(1, len(prev_term)):
            if prev_term[index] == prev_term[index - 1]:
                count += 1
            else:
                next_term += str(count) + prev_term[index - 1]
                count = 1

        next_term += str(count) + prev_term[-1]
        prev_term = next_term

    return prev_term


print(look_and_say(5))
