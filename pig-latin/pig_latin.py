def translate(text: str):
    return ' '.join(translate_word(word) for word in text.split())


def translate_word(word: str):
    VOWELS = 'aeiou'
    
    # Rule 1: Starts with vowel, "xr", or "yt"
    if word[0] in VOWELS or word.startswith(('xr', 'yt')):
        return word + 'ay'
    
    # Find the split point (where to break the word)
    split_index = _find_split_index(word, VOWELS)
    return word[split_index:] + word[:split_index] + 'ay'


def _find_split_index(word: str, vowels: str) -> int:
    """Find the index where to split the word for Pig Latin translation."""
    
    # Rule 3: Handle "qu" patterns
    if word.startswith('qu'):
        return 2
    
    for i in range(1, len(word)):
        # Rule 3: Consonant(s) + "qu" at start
        if word[i:i+2] == 'qu' and all(c not in vowels for c in word[:i]):
            return i + 2
        
        # Rule 4: Consonant cluster + "y" (treat "y" as vowel)
        if word[i] == 'y' and all(c not in vowels for c in word[:i]):
            return i
        
        # Rule 2: Found first vowel
        if word[i] in vowels:
            return i
    
    # No vowel found - return full length
    return len(word)
