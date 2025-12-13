from typing import Final

ACTIONS: Final[list[str]] = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> list[str]:
    num = int(binary_str, 2) if binary_str else 0
    result: list[str] = [ACTIONS[i] for i in range(len(ACTIONS)) if num & (1 << i)]

    return result if not (num & (1 << 4)) else result[::-1]
