import time

def mima(a, b, c, d):
    if c >= 1:
        for i in range(a, b + 1):
            d[c - 1] = i
            mima(a, b, c - 1, d)
    else:
        time.sleep(0.5)
        for i in range(len(d)):
            print(d[i], end=" ")
        print("")


while True:
    a = int(input("端数："))
    mima(int(input("开始：")), int(input("结束：")), a, [0 for x in range(a)])
