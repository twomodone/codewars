def remainder(a,b):
    larger = max(a, b)
    smaller = min(a, b)
    if (smaller == 0):
        return None
    return larger % smaller
