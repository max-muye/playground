while True:
    a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    msg1 = input("请输入:")
    output = ""
    for m in range(len(msg1) + 1):
        d = 0
        if m > len(msg1) - 1:
            d = 1
        if d == 0:
            msg = msg1[m]
        else:
            break
        if msg in b:
            for i in range(10):
                if msg in b[i]:
                    output += a[i]
        if msg in a:
            for i in range(10):
                if msg in a[i]:
                    output += b[i]
    print(output)
