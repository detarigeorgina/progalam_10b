n = int(input("n: "))

primE = True

i = 2 
while i < n and primE:
    if n % i == 0:
        primE == False
        #print(i)
        #print("nem primszam")
    i+= 1

if primE:
    print("Primszam!")
else: 
    print("Nem primszam! legkisebb osztoja:", i-1)