def metszet_kepzes(a, b):
    m = []
    for i in range(len(a)):
        if a[i] in b:
            m.apppend(a[i])
    return m

def unio_kepzes(a, b):
    u = []
    for i in range(len(a)):
        u.append(a[i])

    for i in range (len(b)):
        if b[i] not in a:
            u.append(b[i])
    return u 

def a_minus_b_kepzes(a, b):
    d = []
    for i in range(len(a)):
        if a[i] not in b[i]:
            d.append(a[i])
    return d

matekosok = ["Anna", "Béla", "Csaba", "Dóra", "Erik", "Ferenc"]
progosok = ["Ferenc", "József", "Dóra", "Anna", "Csaba"]
metszet = metszet_kepzes(matekosok, progosok)
print(metszet)

unio = unio_kepzes(matekosok, progosok)
csak_matekos = a_minus_b_kepzes(matekosok, progosok)