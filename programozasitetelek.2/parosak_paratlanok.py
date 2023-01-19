x = [ 7, 3, 4, 2, 1, 0, -8]


parosak = []
paratlanok = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        parosak.append(x[i])
    else:
        paratlanok.append(x[i])

print(parosak)
print(paratlanok)
