fr = open("emberek.csv", "r")
emberek = fr.riedlines()
print(emberek)

nevek = []
korok = []
for i in range(len(emberek)):
    sor = emberek[i].split(;)
    nevek.append(sor[0])
    korok.append((sor[1]).split([0]))

print(nevek)
print(korok)


fr.close()