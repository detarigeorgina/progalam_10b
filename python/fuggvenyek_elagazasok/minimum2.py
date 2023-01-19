def minimum(*lista):
    n = len(lista)

    if n == 0:
        return None
    minert = lista[0]
    for i in range (1, n):
        if lista[i] < minert:
            minert = lista[i]
    return minert
  
m = minimum (6, 7, -1, 7, 13, 8)
print(m)


m2 = minimum()
print(m2)


m3 = minimum(4, 1, 8)
print(m3)