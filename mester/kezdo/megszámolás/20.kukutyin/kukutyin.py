n = int(input())
k = []
p = []
for i in range(n):
    sor = list(map(int, input().split()))
    k.append(sor[0])
    p.append(sor[1])
print(k, p, sep="\n")

#feldolgozás
db = 0
for i in range(n):
    if k[i] <p[1]:
        db += 1

#kiiras
print(db)