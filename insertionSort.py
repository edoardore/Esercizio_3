def insertionSort(A):
    n = len(A)
    for j in range(2, n):
        key = A[j]
        i = j - 1
    while (i >= 0) and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key

