while True:
    msg = float(input("请输入数字:"))
    msg1 = int(msg)
    if msg1!=msg:
        print("错误")
        continue
    e=0
    if msg <= 0:
        e=1
        msg=-msg
    c = 1
    a = c
    while True:
        b = ""
        d = 0
        while True:
            for i in range(a):
                if c <= msg:
                    if e == 1:
                        b+="-"
                    b += str(c)
                    b += " "
                    c += 1
                else:
                    d = 1
                    break
            if d == 1:
                break
            for i in range(a):
                if c <= msg:
                    c += 1
                else:
                    d = 1
                    break
            if d == 1:
                break
        print(b)
        print(" ")
        a *= 2
        c = a
        if c > msg:
            break
