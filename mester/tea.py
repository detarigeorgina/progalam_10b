n = int(input())
f = []
m = []

for i in range(n):
    fajtak = input()
    mennyiseg = int(input())
    f.append(fajtak)
    m.append(mennyiseg)

s = 0
elsoFajta = f[0]
for i in range(n):
    if f[i] == elsoFajta:
        s += m[i]


