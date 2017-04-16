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
        q = (p + r) // 2
        Merge_sort(A, p, q)
        Merge_sort(A, q + 1, r)
        Merge(A, p, q + 1, r)

def Merge(A, p, q, r):
    L = A[p:q]
    R = A[q:r + 1]
    inf = float("inf")
    L.append(inf)
    R.append(inf)
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1