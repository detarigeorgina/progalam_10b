

def egyediek_kivalogatasa(lista):
    h = []
    for i in range(len(lista)):
        if lista[i] not in h: 
            h.append(lista[i])
    return h 


lista = [7, 3, 2, 5, 3, 5, 3, 3]
halmaz = egyediek_kivalogatasa(lista)
print(halmaz)