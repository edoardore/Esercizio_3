from math import modf

def merge(A, p, r):
    if p < r:
        dec, q = modf((p + r) / 2)
        merge(A, p, q)
        merge(A, q + 1, r)
        mergeSort(A, p, q, r)

def mergeSort(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0]
    R = [0]
    for i in range(1, n1):
        L[i] = A[p + i - 1]
    for j in range(1, n2):
        R[j] = A[q + j]
    L[n1 + 1] = max(L) + 1
    R[n2 + 1] = max(R) + 1
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
        i += 1
    else:
        A[k] = R[j]
        j += 1
