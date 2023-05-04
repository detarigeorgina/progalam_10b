def beolvas(o, sze, szi):
    fr = open("kerites.txt", "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.split()
        o.append(int(sor[0]))
        sze.append(int(sor[1]))
        szi.append(int(sor[2]))
        sor = fr.readline()
    fr.close()

def ki(n):
    print("\n" + str(n) + ". feladat")

def feladat2(x):
    ki(2)
    print("eladott telkek szama:", len(x))

def feladat3(oldalak):
    ki(3)
    paros, paratlan = 0, -1
    for i in range(oldalak):
        if oldalak[i] == 0:
            sorszam = int(input())
            print(sorszam + 2)
        elif oldalak[i] == 1:
            sorszam = int(input())
            print(sorszam + 1)
        



def main():
    oldalak, szelessegek, szinek = [], [], []
    feladat2(oldalak)
    feladat3(oldalak)
    hszamok = []
    paratlanok, parosok = [], []
    feladat3(oldalak, hszamok, paratlanok, parosok)
 
main()