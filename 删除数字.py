while True:
    msg, res = list(input()), ["0"]
    msg1 = msg[:]
    for i in range(int(input()) + 1, len(msg) + 1):
        cm = msg[:]
        for j in range(len(msg1) - i):
            cm.pop()
        res.append(min(cm))
        for j in range(cm.index(min(cm)) + 1):
            msg.pop(0)
    print(int("".join(res)))
