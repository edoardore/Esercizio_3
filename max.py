def max(A):
    massimo = A[0]
    pos = 1
    while pos < len(A):
        if A[pos] > massimo:
            massimo = A[pos]
        pos = pos + 1
    return massimo
