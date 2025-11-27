def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Convert to decimal
    decimal: int = sum(digit * input_base**i for i, digit in enumerate(reversed(digits)))

    if decimal == 0:
        return [0]

    # Convert from decimal to output_base
    result: list[int] = []
    while decimal:
        decimal, remainder = divmod(decimal, output_base)
        result.append(remainder)

    return result[::-1]
