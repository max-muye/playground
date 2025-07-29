while True:
    a, b, c, d, e, f, g = [], input(), ["(", "[", "{"], {")": "(", "]": "[", "}": "{"}, "YES", 0, 0
    for i in b:
        if i in c:
            a.append(i)
            f += 1
        elif len(a) > 0 and a[-1] == d[i]:
            a.pop()
            g += 1
        else:
            e = "NO"
            break
    if f == g:
        print(e)
    else:
        print("NO")
