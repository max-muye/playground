while True:
    msg = int(input())
    for i in range(msg):
        for j in range(msg):
            if i * 5 + j * 3 + (msg - i - j) / 3 == msg:
                print(i, j, msg - i - j)
