def minindex(x, i):
    mini = i
    for j in range(i+1, len(x)):
        if x[j] < x[mini]:
            mini = j
    return mini


def rendezes_minimum(x):
    for i in range(len(x)-1):
        mini = minindex(x, i)
        # seged = x[i]
        # x[i] = x[mini]
        # x[mini] = seged

    x[i], x[mini] = x[mini], x[i]

def main():
    x = [3, 5, 2, 1, 3]
    print(x)
    rendezes_minimum(x)
    print(x)

main()