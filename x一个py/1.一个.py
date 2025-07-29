while True:
    input()
    k=int(input())
    A=[int(x) for x in input().split()]
    for i in range(len(A)):
        if A[i]>k:
            A[i]=max(A)
        elif A[i]<k:
            A[i]=min(A)
    for i in A:
        print(i,end=" ")
    print()
