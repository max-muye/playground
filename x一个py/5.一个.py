a,b,c=map(int,input().split())
res=[[] for x in range(a+1)]

for i in range(b):
    d,e=map(int,input().split())
    res[d].append(str(e))
    res[e].append(str(d))

for i in range(c):
    f=int(input())
    print(len(res[f]),"\n"," ".join(res[f]),sep="")
    print()
    