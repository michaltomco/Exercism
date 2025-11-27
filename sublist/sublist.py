"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list[int], list_two: list[int]):
    if list_one == list_two:
        return EQUAL

    if not list_one:
        return SUBLIST

    if not list_two:
        return SUPERLIST

    shorter, longer = (
        (list_one, list_two) if len(list_one) < len(list_two) else (list_two, list_one)
    )

    for i in range(len(longer) - len(shorter) + 1):
        if shorter == longer[i : i + len(shorter)]:
            return SUBLIST if shorter is list_one else SUPERLIST

    return UNEQUAL
