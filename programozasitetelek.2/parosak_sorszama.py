x = [ 7, 3, 4, 2, 1, 0, -8]

#kiválogatas
y = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        y.append(i+1)

#kiiras
print(x)
print(y)

