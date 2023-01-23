#halmazkeszites tétel(egyediek kiválogatasa)
def bennevan(lista:list, elem:int):
    i = 0
    n = len(lista)
    while i < n and not(lista[i] == elem):
        i += 1
    return i < n 

def egyediek_kivalogatasa(lista):
    h = []
    for i in range(len(lista)):
        if not bennevan(h,lista[i]): 
            h.append(lista[i])
    return h 


lista = [7, 3, 2, 5, 3, 5, 3, 3]
halmaz = egyediek_kivalogatasa(lista)
print(halmaz)