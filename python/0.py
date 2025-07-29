input = [1,5,3,7,6,4,9,0,2,8]
b = input
a = len(b)
c=""
for u in range(a):
    a = 0
    for i in range(len(b)):
        msg = b[i]
        if a < msg:
            a = msg
    c+=str(a)
    c+=" "
    b.remove(a)
print(c)
