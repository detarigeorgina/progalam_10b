n = int(input())

magassag = []
ev = []

for i in range(n):
    sor = list(map(int, input().split()))
    ev.append(sor[0])
    magassag.append(sor[1])
print(magassag, ev)


