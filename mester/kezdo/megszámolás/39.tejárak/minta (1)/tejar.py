be = input()
lista = be.split()
szamok = list(map(int, lista))
"""print(szamok)"""

n = szamok[0] #6
p = szamok[1] #200
q = szamok[2] #220

#tejarak beolvasasa
tejarak = []
for i in range(n):
    ar = int(input())
    tejarak.append(ar)
'''print(tejarak)'''

#feldolgozás (megszamolas tetel)
db = 0
for i in range(n):
    if p <= tejarak[i] and tejarak[i] <= q:
        db += 1

    
#kiiras
print(db)
        



