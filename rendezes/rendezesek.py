from random import randint
from minimum_kivalasztasos import rendezes_minimum
from buborekos import buborekos
from os import system 
from time import time


def feltolt(n):
    x = []
    for i in range(n):
        r = randint(1,20)
        x.append(r)
    return x

def main():
    #kepernyo törlés
    system("cls")
    x = feltolt(10)

    print("\nRendezes elott:")
    print(x)

    y = x.copy()
    start = time()
    rendezes_minimum(y)
    stop = time()
    print("\nMinimum_kivalasztasa")
    print("ido:", round(stop - start, 20))


    rendezes_minimum(x)
    print("\nminimum kivalasztasos:")
    print(x)

    y = x.copy()
    buborekos(x)
    print("\nbuborekos:")
    print(y)

    y = x.copy()
    y.sort()
    print("\nLista sort")
    print(y)


# main()