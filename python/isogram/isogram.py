def is_isogram(string: str):
    letters = string.lower().replace(" ","").replace("-","")
    return len(letters) == len(set(letters))