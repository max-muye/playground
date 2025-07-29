import random as r
c=[0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000000):
    a=r.randint(1,6)
    b=r.randint(1,6)
    a=a+b
    b=c[a]
    b+=1
    c[a]=b
for i in range(2,13):
    print(i,c[i])
