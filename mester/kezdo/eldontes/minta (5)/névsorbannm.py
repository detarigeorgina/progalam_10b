n = int(input)
nevek = []
magassagok = []
for i in range(n):
    sor = input().split()
    print = (sor)
    nevek.append(sor[0])
    magassagok.append(int(sor[1]))
# print(nevek, magassagok)

#eldontes

i = 1
while i < n and not(magassagok[i] < magassagok [i-1]):
    i += 1
if i < n:
    print("NEM")
else:
    print("IGEN")

osszeg = 0
for i in range(1, n):
    osszeg += magassagok[i]
    atlag = osszeg / n 

    magasakDb = 0
    for i in range(n):
        if atlag <magassagok[i]:
            magasakDb += 1
print("alagnal magasabbak:" magasakDb)