def rotate(text: str, key: int) -> str:
    result = []
    for char in text:
        if char.islower():
            result.append(chr((ord(char) - ord('a') + key) % 26 + ord('a')))
        elif char.isupper():
            result.append(chr((ord(char) - ord('A') + key) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)
