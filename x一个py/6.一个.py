a,b,c=map(int,input().split())
res1=[[] for x in range(a+1)]
res2=[[] for x in range(a+1)]
for i in range(b):
    d,e=map(int,input().split())
    res1[d].append(str(e))
    res2[e].append(str(d))

for i in range(c):
    f=int(input())
    print(len(res1[f]),"\n"," ".join(res1[f]),sep="")
    print(len(res2[f]),"\n"," ".join(res2[f]),sep="")
    print()
    