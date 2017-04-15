from Sort import Insertion_sort
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

def random_list_backwards(n):
    A = range(n)
    A.reverse()
    return A

# con questi parametri si vede molto bene la crescita quadratica (Caso medio)
def TestInsShuffle():
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
            Insertion_sort(B)
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
    plt.xlabel('Insertion Sort su dati disposti casualmente')
    plt.show()

# con questi parametri si vede molto bene la crescita lineare (Caso Ottimo)
def TestInsOrdered():
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
            Insertion_sort(B)
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
    plt.xlabel('Insertion Sort su dati ordinati')
    plt.show()

# con questi parametri si vede molto bene la crescita quadratica (Caso Peggiore)
def TestInsBackwards():
    M = []
    T = []
    ind = 0
    dimensione = 10
    while ind < 200:  # mettere 3 per ottenere 10, 100, 1000
        A = random_list_backwards(dimensione)
        i = 0
        while i < 5:
            B = A
            start = timer()
            Insertion_sort(B)
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
    plt.xlabel('Insertion Sort su dati ordinati al contrario')
    plt.show()
