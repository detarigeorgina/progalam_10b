fr = open("adatok.txt", "r")
szamok = fr.read().split("\n")
for i in range(len(szamok)):
    szamok[i] = int(szamok[i])
# map(int,szamok)
print(szamok)
fr.close()