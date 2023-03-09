def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        if k == 1:
            return int(n)
        else:
            return superDigit(str(int(n) * k), 1)
    number = 0
    for digit in n:
        number += int(digit)
    n = str(number)
    return superDigit(n, k)