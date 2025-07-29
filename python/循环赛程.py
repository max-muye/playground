import math

while True:
    msg = int(input("请输入队员个数:"))
    msg_2 = int(math.log2(msg))
    res = [[0 for i in range(msg)] for j in range(msg)]

    res[0][0] = 1

    for i in range(msg_2):
        for y in range(2**i):
            for x in range(2**i):
                res[2**i + y][x] = res[y][x] + 2**i
        for y in range(2**i):
            for x in range(2**i):
                res[y][2**i + x] = res[y + 2**i][x]
        for y in range(2**i):
            for x in range(2**i):
                res[2**i + y][2**i + x] = res[y][x]

    for i in res:
        for j in i:
            print(f"{j:2d}", end=" ")
        print()
