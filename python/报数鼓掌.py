while True:
    msg = int(input())
    a = 0
    for i in range(1, msg + 1):
        if "3" not in str(i) and i / 3 != i // 3:
            a += 1
    print(a)
