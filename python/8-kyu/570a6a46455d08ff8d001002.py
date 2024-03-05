def no_boring_zeros(n):
    if n == 0:
        return n
    while (True):
        if (n % 10 != 0):
            return n
        n /= 10
