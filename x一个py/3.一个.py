while True:
    msg=[int(x) for x in input().split()]
    now_num,has_num=msg[0],msg[0]
    while has_num>msg[1]-1:
        now_num,has_num=now_num+int(has_num/msg[1]),int(has_num/msg[1])
    print(now_num)
