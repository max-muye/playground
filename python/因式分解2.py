while True:
    d = ""
    msg = int(input("请输入:"))
    for a in range(2, msg - 1):
        while True:
            b = msg / a
            c = msg // a
            if c == b:
                msg = c
                d += str(a) + " "
            else:
                break
    if d == "":
        print("这个数是质数，无法因式分解")
    else:
        print(d)
