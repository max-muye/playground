def lt(k, j, c):
    if k==0:
        return "无限"
    global a, z
    if z < c:
        for i in range(k, j + 1):

            z += i
            lt(k, j, c)
            z -= i
    elif z == c:
        a += 1
    return a
while True:
    a, z = 0, 0
    print(lt(int(input("开始：")),int(input("结束：")),int(input("层数："))))
