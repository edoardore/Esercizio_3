from math import modf

def Insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def max(A):
    massimo = A[0]
    pos = 1
    while pos < len(A):
        if A[pos] > massimo:
            massimo = A[pos]
        pos = pos + 1
    return massimo


def Merge_sort(A, p, r):
    if p < r:
        dec, q = modf((p + r) / 2)
        q = int(q)
        Merge_sort(A, p, q)
        Merge_sort(A, q + 1, r)
        Merge(A, p, q, r)


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    i = 0
    j = 0
    while i <= n1:
        L.append(A[p + i])
        i += 1
    while j <= n2:
        R.append(A[q + j])
        j += 1
    L.append(max(L) + 1)
    R.append(max(R) + 1)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
