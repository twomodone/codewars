def position(alphabet):
    letters = "abcdefghijklmnopqrstuvwxyz"
    if alphabet in letters:
        return f"Position of alphabet: {letters.index(alphabet) + 1}"
