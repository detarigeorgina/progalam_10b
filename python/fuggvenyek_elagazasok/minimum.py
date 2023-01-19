def minimum(lista):
    n = len(lista)

    if n == 0:
        return None
    minert = lista[0]
    for i in range (1, n):
        if lista[i] < minert:
            minert = lista[i]
    return minert
  
x = [6, 7, -1, 7, 13, 8]
m = minimum(x)
print(m)

y = []
m2 = minimum(y)
print(m2)