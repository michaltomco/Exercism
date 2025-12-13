from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_folded: str = word.casefold()
    word_counter: Counter[str] = Counter(word_folded)

    return [
        candidate
        for candidate in candidates
        if candidate.casefold() != word_folded
        and Counter(candidate.casefold()) == word_counter
    ]
