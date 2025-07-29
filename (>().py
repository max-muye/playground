while True:
    a, b, c, d, e = input(), ["(", "[", "{"], {")": "(", "]": "[", "}": "{", "(": ")", "[": "]", "{": "}"}, "", ""
    for i in a:
        if i in b:
            d = c[i]
            e += i + d
        elif i == d:
            d = ""
        else:
            e += c[i] + i
    print(e)