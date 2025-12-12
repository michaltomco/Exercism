from string import ascii_lowercase, punctuation, whitespace
from typing import Final

CIPHER: Final[dict[int, int | None]] = str.maketrans(
    ascii_lowercase, ascii_lowercase[::-1],
    punctuation + whitespace)
CHUNK_SIZE: Final[int] = 5


def encode(plain_text: str) -> str:
    encoded: str = plain_text.lower().translate(CIPHER)
    return " ".join(
        encoded[i : i + CHUNK_SIZE] for i in range(0, len(encoded), CHUNK_SIZE)
    )


def decode(ciphered_text: str) -> str:
    return ciphered_text.replace(" ", "").translate(CIPHER)
