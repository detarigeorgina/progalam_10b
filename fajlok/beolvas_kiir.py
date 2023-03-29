from random import randint

'''
#Beolvasas - konzolrol
n = int(input())
szamok = []
for i in range(n):
    szamok.append(float(input()))
print(szamok)
print(randint(1, 20))
'''

#Olvasasra megnyitok egy fajlt
fr = open("be.txt", "r")
n = int(fr.readline())
szamok = []
for i in range(n):
    szamok.append(float(fr.readline()))
fr.close()

#irasra megnyitok eg yfajlt
fw = open("ki.txt" "w")
for i in range(len(szamok)):
    fw.write(str(szamok[i]) + "\n")
fw.write(str(randint(1,20)))
fw.close()

#hozzafuzni meglevo fajl vegehez
fw = open("ki.txt", "w")
for i in range(len(szamok)):
    fw.write(str(szamok[i]) + "\n")
fw.write(str(randint(1, 20)))
fw.close()

f = open("teszt.txt", "r+")
a = int(f.readline())
b = int(f.readline())
c = int(f.readline())
#print(a, b, c)
f.write(str(a) + " " + str(b) + " " + str(c))
f.close()