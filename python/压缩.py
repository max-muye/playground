def yasuo(c):
    a = {}
    b = 0
    for i in range(97, 124):
        for j in range(97, 124):
            if i != 123 and j != 123:
                a.update({chr(i) + chr(j): b})
            elif i != 123:
                a.update({chr(i) + " ": b})
            elif j != 123:
                a.update({" " + chr(j): b})
            else:
                a.update({"  ": b})
            b += 1

    d = ""
    f = 0

    for i in range(len(c) // 2):
        d = d + str(a[c[f] + c[f + 1]]) + " "
        f += 2

    if len(c) % 2 != 0:
        h = 729
        o = {}
        for i in range(97, 124):
            if i != 123:
                o.update({chr(i): h})
            else:
                o.update({" ": h})
            h += 1
        o.update({703: " "})

        d = d + str(o[c[len(c) - 1]]) + " "

    return d


def jieya(a):
    b = {}
    c = 0
    z = ""
    for i in range(97, 124):
        for j in range(97, 124):
            if i != 123 and j != 123:
                b.update({c: chr(i) + chr(j)})
            elif i != 123:
                b.update({c: chr(i) + " "})
            elif j != 123:
                b.update({c: " " + chr(j)})
            else:
                b.update({c: "  "})
            c += 1

    for i in range(len(a)):
        if a[i] >= 729:
            break
        z += b[a[i]]

    if a[len(a) - 1] >= 729:
        o = 729
        p = {}
        for i in range(97, 123):
            p.update({o: chr(i)})
            o += 1
        z += p[a[len(a) - 1]]
    return z


while True:
    print(yasuo(input()))
    print(jieya([int(x) for x in input().split()]))
