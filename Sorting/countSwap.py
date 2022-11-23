def countSwaps(a):
    # Write your code here
    numSwamp = 0
    # print(a)
    for i in range(1, len(a)):
        for j in range(0, len(a) - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwamp += 1
    
    print("Array is sorted in {} swaps.".format(numSwamp))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a) - 1]))  


lists = [4, 3, 2, 1]
countSwaps(lists)