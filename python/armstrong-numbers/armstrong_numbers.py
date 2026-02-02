def is_armstrong_number(number):
    """Determine if a number is an Armstrong number.

    An Armstrong number is an n-digit number that is equal to the sum of the nth
    powers of its digits.

    :param number: int - The number to check.
    :return: bool - True if the number is an Armstrong number, False otherwise.
    """
    # digits = [int(d) for d in str(number)]
    # num_digits = len(digits)
    # armstrong_sum = sum(d ** num_digits for d in digits)
    # return armstrong_sum == number
    num_digits = len(str(abs(number)))
    digits = [number % 10 ** d // 10 ** (d - 1) for d in range(1, num_digits+1)]
    armstrong_sum = sum(d ** num_digits for d in digits)
    return armstrong_sum == number
