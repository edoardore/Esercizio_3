from Sort import Merge_sort
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def random_list_shuffle(n):
    A = range(n)
    random.shuffle(A)
    return A

def random_list(n):
    A = range(n)
    return A

def TestMergeSortShuffle():
    M = []
    T = []
    ind = 0
    dimensione = 10
    while ind < 200:  # mettere 3 per ottenere 10, 100, 1000
        A = random_list_shuffle(dimensione)
        i = 0
        while i < 5:
            B = A
            start = timer()
            Merge_sort(B, 0, dimensione - 1)
            end = timer()
            time = end - start
            T.append(time);
            i += 1
        dim = len(T)
        sum = 0
        for i in range(0, dim):
            sum += T[i]
        media = sum / dim
        M.append(media)
        ind += 1
        dimensione += 10  # mettere *= 10 al posto di += 10 per ottenere 10, 100, 100
    plt.plot(M)
    plt.ylabel('Secondi')
    plt.xlabel('Merge Sort Caso Medio')
    plt.show()

def TestMergeSortOrdered():
    M = []
    T = []
    ind = 0
    dimensione = 10
    while ind < 200:  # mettere 3 per ottenere 10, 100, 1000
        A = random_list(dimensione)
        i = 0
        while i < 5:
            B = A
            start = timer()
            Merge_sort(B, 0, dimensione - 1)
            end = timer()
            time = end - start
            T.append(time);
            i += 1
        dim = len(T)
        sum = 0
        for i in range(0, dim):
            sum += T[i]
        media = sum / dim
        M.append(media)
        ind += 1
        dimensione += 10  # mettere *= 10 al posto di += 10 per ottenere 10, 100, 100
    plt.plot(M)
    plt.ylabel('Secondi')
    plt.xlabel('Merge Sort Caso Ottimo')
    plt.show()
