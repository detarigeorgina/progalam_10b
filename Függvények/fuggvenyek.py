def beolvas(szamok: list):
    fr = open("adatok.txt", "r")
    sor = fr.readline().strip()
    while sor != "":
        szamok.append(int(sor))
        sor = fr.readline().strip()
    fr.close()

def beolvas2(szamok: list):
    fr = open("adatok.txt", "r")
    szamok += map(int, fr.readlines())
    fr.close()

#source manager
def beolvas3(szamok: list):
    with open("adatok.txt", "r") as fr:
        szamok += map(int, fr.readlines())

def pozitivak_kivalogat(szamok: list):
    pozitivak = []
    for i in range(len(szamok)):
        if szamok[i] > 0:
            pozitivak.append(szamok[i])
    return pozitivak

def nagyobbak_szama(szamok: list, k = 0):
    db = 0
    for i in range(len(szamok)):
        if szamok[i] > k: 
            db += 1
    return db



def main():
    szamok = []
    beolvas3(szamok)
    print(szamok)
    
    print(pozitivak_kivalogat([4, -1, 0, 7, 5]))

    print(nagyobbak_szama([4, -1, 0, 7, 5], 4))
    print(nagyobbak_szama([4, -1, 0, 7, 5]))

main()

