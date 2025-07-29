input = [x for x in range(101)]
b = input
a=len(b)//2
for u in range(a):
    a = 0
    for i in range(len(b)):
        msg = b[i]
        if a < msg:
            a = msg
    c = a
    b.remove(a)
print(c)
