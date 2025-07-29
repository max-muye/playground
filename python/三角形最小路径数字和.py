while True:
    a = []
    for i in range(int(input()), 0, -1):
        a.append([int(x) for x in input(" " * (i - 1)).split()])
    b = a
    c=[]
    for i in range(1, len(a)):
        for j in range(i + 1):
            if j == 0:
                b[i][j] = b[i - 1][j] + a[i][j]
            elif i == j:
                b[i][j] = b[i - 1][j - 1] + a[i][j]
            else:
                b[i][j] = min(b[i - 1][j], b[i - 1][j - 1]) + a[i][j]
    print(min(b[len(b) - 1]))
