def replace_exclamation(st):
    new_str = ""
    vowels = "aeiouAEIOU"
    for ch in st:
        if ch in vowels:
            new_str += '!'
        else:
            new_str += ch
    return new_str
