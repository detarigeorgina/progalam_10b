def kivalogat(minek, maxok):
    lista = []
    for i in range(len(minek)):
        if minek[i] < 0 and maxok[i] >= 0:
            lista.append(i)
    return lista

def kiir(lista):
    print(len(lista), end=" ")
    for i in range(len(lista)):
        print(lista[i]+1, end= " ")

def main():
    #Beolvasas
    n = int(input())
    minek = []
    maxok = []
    for i in range(n):
        sor = input().split()
        minek.append(int(sor[0]))
        maxok.append(int(sor[1]))
    
    fagyasok_olvadasok = kivalogat(minek, maxok)
    kiir(fagyasok_olvadasok)

main()