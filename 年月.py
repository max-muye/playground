while True:
    msg = input().split()
    if int(msg[1]) == 4 or int(msg[1]) == 6 or int(msg[1]) == 9 or int(msg[1]) == 11:
        print(31)
    elif int(msg[1]) == 2:
        if int(msg[0]) % 4 == 0 and int(msg[0]) % 100 != 0 or int(msg[0]) % 400 == 0:
            print(29)
        else:
            print(28)
    else:
        print(31)
