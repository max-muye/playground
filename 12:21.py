while True:
    msg = input()
    b=0
    if msg[0] == "-":
        msg=int(msg)
        msg=abs(msg)
        msg=str(msg)
        b=1
    a = ""
    for i in range(len(msg) - 1, -1, -1):
        a += msg[i]
    if b==1:
        a=int(a)
        a=-a
        a=str(a)
    print(int(a))
    print("")
