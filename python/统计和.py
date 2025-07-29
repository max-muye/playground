while True:
    n = int(input("N"))
    m = int(input("M:"))
    a = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if i + j > m:
                a += 1
    print(a)
