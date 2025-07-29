while True:
    max_msg=int(input())
    msg=[]
    
    for i in range(int(input())):
        msg.append(int(input()))
    res=len(msg)
    for i in msg:
        a=max_msg-min(msg)
        b=[]
        for j in msg:
            b.append(j) if j <=a else None
        res-=1 if b else None
        msg.remove(min(msg))
        msg.remove(max(b))
    print(res)
        