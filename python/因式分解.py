while True:
    msg = int(input("请输入:"))
    for a in range(1, msg + 1):
        b = msg / a
        c = msg // a
        if c == b:
            print(a)
