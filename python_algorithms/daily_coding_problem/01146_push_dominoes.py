"""
You are given an string representing the initial conditions of some dominoes. Each element can
take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a domino
receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""


def push_dominoes(dominoes: str) -> str:
    length = len(dominoes)
    forces = [0] * length

    # right forces (R)
    force = 0
    for index in range(length):
        if dominoes[index] == "R":
            force = length
        elif dominoes[index] == "L":
            force = 0
        else:
            force = max(force - 1, 0)

        forces[index] += force

    # left forces (L)
    force = 0
    for index in range(length - 1, -1, -1):
        if dominoes[index] == "L":
            force = length
        elif dominoes[index] == "R":
            force = 0
        else:
            force = max(force - 1, 0)

        forces[index] -= force

    # determine final state
    result = []
    for force in forces:
        if force == 0:
            result.append(".")
        elif force > 0:
            result.append("R")
        else:
            result.append("L")

    return "".join(result)


print(push_dominoes(".L.R....L"))  # Output: "LL.RRRLLL"
print(push_dominoes("..R...L.L"))  # Output: "..RR.LLLL"
