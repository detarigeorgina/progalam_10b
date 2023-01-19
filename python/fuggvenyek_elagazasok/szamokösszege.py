def beolvasas(x):
    n = int(input())
    x.append(n)
    while n % 3 != 0:
        x.append(n)
        n = int(input())

def osszeg(l):
    osszeg = 0
    for i in range(len(l)):
        osszeg += l[i]
    return osszeg

def kiir(s):
    print("A lista elemeinek osszege:", s)

lista = []
beolvasas(lista)
s = osszeg(lista)
kiir[s]
# print(lista)

