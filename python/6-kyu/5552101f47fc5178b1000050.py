def dig_pow(n, p):
    n_string = str(n)
    sum = 0
    for digit in n_string:
        sum += int(digit) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1
