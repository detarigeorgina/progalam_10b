n = int(input())

h = []
p = []
Mp = []

for i in range(n):
    sor = list(map(int, input().split()))
    h.append(sor[0])
    p.append(sor[1])
    Mp.append(sor[2])
print(h, p, Mp)

mine = 0
for i in range(1, n):
    if h[i] <= mine:
        mine = i


db = 0
for i in range(n):
    if h[i] == mine[i]:
        db =+ 1

print(mine, db)