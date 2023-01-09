x = [7, 9, 12, 3, -5, -2, 8, -5, 18, -1]
n = len(x)

db = 0

for i in range(n):
    if x[i] % 2 == 0:
        db += 1

print("Parosok szama:", db)


maxe = x[0]
for i in range(1, n):
    if x[i] >maxe:
        maxe = x[i]
    
print("Legnagyobb elem:" maxe)


szorzat = 1
for i in range(n):
    if x[i] < 0:
        szorzat *= x[i]
print("Negativ szorzata:" szorzat)


min = 0
for i in range(1, n):
    if x[i] <= x[min]:
        mini = 1
print("legkisebb elem indexe:", mini+1)

s = 0
for i in range(n):
    s = x[i]
    atlag = s / n
print("atlag:", atlag)