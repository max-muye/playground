while True:
    a,b,c=map(int,input().split())
    d=[]
    for i in range(c):
        d.append([int(x) for x in input().split()])
    c=[[1 for i in range(b+1)] for i in range(a+1)]
    e,f=[1,2,2,1,-1,-2,-2,-1],[-2,-1,1,2,2,1,-1,-2]
    for i in d:
        if 0<=i[0]<=a and 0<=i[1]<=b:
            c[i[0]][i[1]]=0
        for j in range(8):
            if 0<=i[0]+e[j]<=a and 0<=i[1]+f[j]<=b:
                c[i[0]+e[j]][i[1]+f[j]]=0
    e=[[0 for i in range(b+1)] for i in range(a+1)]
    e[0][1]=1
    for i in range(1,a+1):
        for j in range(1,b+1):
            if c[i][j]==1:
                e[i][j]=e[i-1][j]+e[i][j-1]
    print(e[a][b])
