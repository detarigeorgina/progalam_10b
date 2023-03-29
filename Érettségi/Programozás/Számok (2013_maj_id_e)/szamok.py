from random import randint


def beolvas(k, v, p, t):
    fr = open ("felszam.txt", "r")
    kerdes = fr.readline().strip()
    while kerdes != "":
        k.append(kerdes)
        valasz = fr.readline().strip()
        valasz = valasz.strip()
        v.append(int(valasz[0]))
        p.append(int(valasz[1]))
        t.append(valasz[2])
        kerdes = fr.readline().strip()
    fr.close()
    print(v)


def feladat2(kerdesek):
    print("\n2.feladat")
    print("az adatfajlban", len(kerdesek), "feladat van.")


def feladat3(p, t):
    print("\n3. feladat")
    db = 0
    p1,p2,p3 = 0, 0, 0
    for i in range(len(t)):
        if t[i] == "matematika":
            db +=1
        elif p[i] == 2:
            p2 += 1
        else:
            p3 += 1
    print("az adatfajlban", db, "matematika feladat van, 1 pontot er", p1, "feladat, 2 pontot er", p2, "feladat, 3 pontot er", p3, "feladat.")


def feladat4(v):
    minert = v[0]
    maxert = v[0]
    for i in range(1, len(v)):
        if v[i] < minert:
            minert = v[i]
        if v[i] > maxert:
            maxert = v[i]
    print("A feladat szamerteke ", minert, "-tol ", maxert, "-ig terjed.", sep = "")


def feladat5(temak):
    print("\n5. feladat")
    egyediek = []
    for i in range(len(temak)):
        if temak[i] not in egyediek:
            egyediek.append(temak[i])
    for i in range(len(egyediek)):
        print(egyediek[i])

def kivalogat(temak, tema):
    kivalogatottak = []
    for i in range(len(temak)):
        if temak[i] == tema:
            kivalogatottak.append(i)
    return kivalogatottak



def feladat6(temak, kerdesek, pontok, valaszok):
    print("\n6.feladat")
    tema = input("Milyen temakorbol akarsz kerdest kapni? ")
    sorszamok = kivalogat(temak, tema)
    r = randint(0, len(sorszamok)-1)
    index = sorszamok[r]
    print(kerdesek[index], end=" ")
    valasz = int(input())
    if valasz == valaszok[index]:
        print("A valasz" + str(pontok[index]) + "pontot er. ")
    else:
        print("A valasz 0 pontot er.")
        print("A helyes valasz" + str(valaszok[index]))


def main():
    kerdesek = []
    valaszok = []
    pontok = []
    temak = []
    beolvas(kerdesek, valaszok, pontok, temak)
    print(kerdesek)
    print(pontok)
    print(temak)
    feladat2(kerdesek)
    feladat3(pontok, temak)
    feladat4(valaszok)
    feladat5(temak)
    feladat6(temak, kerdesek, pontok, valaszok)

main()



