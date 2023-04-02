testcases = int(input())
for _ in range(testcases):
    x = int(input())
    # for first condtion a number with the first 1 bit of x will make sure it
    # for the second condition toggle the first rightmost bit of the number that is not the first 1 bit of the number
    y = x & (-x) # for first condition
    
    if not (x ^ y):
        if y & 1:
            y |= 1 << 1 # y += 2, y = 3
        else:
            y |= 1 # y += 1
    print(y)