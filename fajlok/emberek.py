fr = open("emberek.txt", "r")
emberek = fr.riedlines()
# print(emberek)

nevek = []
korok = []
for i in range(len(emberek)):
    sor = emberek[i].split()
    nevek.append(sor[0])
    korok .append(int(sor[1]))
fr.close()