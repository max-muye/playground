while True:
    msg = input()
    msg1 = input()
    b = 0
    for i in range(len(msg) - len(msg1) + 1):
        a = msg[i : i + len(msg1) : 1]
        if a == msg1:
            b += 1
    if b != 0:
        print("yes", b)
    else:
        print("no")
