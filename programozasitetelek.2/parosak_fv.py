def parosak_kivalogatasa(x):
    y = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            y.append(i)
    return y

x = [ 7, 3, 4, 2, 1, 0, -8]

#kivalogatasa
parosak = parosak_kivalogatasa(x)

print(parosak)