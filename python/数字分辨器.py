while True:
    a = [chr(x) for x in range(97, 123)]
    a.append(" ")
    b = [chr(x) for x in range(48, 58)]
    c = []
    msg = input("请输入:")
    if len(msg) == 0:
        print("错误")
        continue
    for i in range(len(msg)):
        if msg[i] in a:
            c.append(1)
        elif msg[i] in b:
            c.append(2)
        else:
            c.append(3)
    d = c[0]
    for i in range(1, len(c)):
        if d != c[i]:
            print("错误")
            break
    else:
        if d == 1:
            print("是字母")
        elif d == 2:
            print("是数字")
        else:
            print("错误")
