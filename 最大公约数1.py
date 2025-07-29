while True:
    msg1 = int(input())
    msg11 = []
    msg2 = int(input())
    msg21 = []

    for i in range(1, msg1 + 1):
        if msg1 / i == msg1 // i:
            msg11.append(i)

    for i in range(1, msg2 + 1):
        if msg2 / i == msg2 // i:
            msg21.append(i)

    a = 0

    for i in msg11:
        for j in msg21:
            if i == j:
                a = i

    print(a)
