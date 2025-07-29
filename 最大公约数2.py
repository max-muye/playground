def gcd(a, b):
    c = a % b
    if c == 0:
        print(a, "/", b, "=", a // b, "~~~~~~", a % b)
        return b
    print(a, "/", b, "=", a // b, "~~~~~~", a % b)
    return gcd(b, c)

while True:
    print(gcd(int(input()), int(input())))

