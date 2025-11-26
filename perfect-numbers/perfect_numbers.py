PERFECT: str = "perfect"
ABUNDANT: str = "abundant"
DEFICIENT: str = "deficient"


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return DEFICIENT

    aliquot_sum: int = 1

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            aliquot_sum += i
            if i != number // i:
                aliquot_sum += number // i
    if aliquot_sum == number:
        return PERFECT
    if aliquot_sum > number:
        return ABUNDANT
    return DEFICIENT
