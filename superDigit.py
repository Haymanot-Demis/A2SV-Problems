def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return int(n)
    number = 0
    for digit in n:
        number += int(digit)
    n = str(number * k)
    return superDigit(n, 1)