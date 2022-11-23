def insertionSort1(n, arr):
    # Write your code here
    j = n - 1
    key = arr[j]
    while(j >= 1 and arr[j - 1] > key):
        arr[j] = arr[j - 1]
        j -= 1
        for el in arr:
            print(el, end=' ')
        print()
    arr[j] = key
    for el in arr:
        print(el, end=' ')

    
insertionSort1(6, [2, 3, 4, 6, 8, 0])