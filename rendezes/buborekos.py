def buborekos(x):
    for i in range(len(x)-1, 0, -1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

def main():
    x = [3, 5, 2, 1, 3]
    print(x)
    buborekos(x)
    print(x)

# main()