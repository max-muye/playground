def aa():
    a, b = int(input()), int(input())
    print(abs(a - b), "\n", a + b, sep="")


def ab():
    msg = [int(i) for i in input().split()]
    a = 0
    for i in msg:
        a += i
    print(round(a / len(msg)))


def ac():
    a, b = int(input()), int(input())
    for i in range(2, a * b):
        if i % a == 0 and i % b == 0:
            print(i)
            break


def ba():
    a, b, c = input(), input(), input()
    print(max(a, b, c))


def bb():
    a = [int(i) for i in input().split()]
    for i in a:
        if i % 2 == 0:
            print(i)


def bc():
    a = 0
    for i in range(1, int(input()) + 1):
        if i % 3 != 0 and "3" not in str(i):
            a += 1
    print(a)


def aaa():
    aa()
    ab()
    ac()


def bbb():
    ba()
    bb()
    bc()


while True:
    bbb()
