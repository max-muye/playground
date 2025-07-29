while True:
    a="yes"
    msg = input()
    for i in msg:
        if i == "0" or int(msg) % int(i) != 0 or len(msg) != 3:
            a="no"
            
    print(a)
