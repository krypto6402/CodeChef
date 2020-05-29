t=int(input())

for t1 in range(t):
    n=int(input())
    lst=[]
    for i in range(n):
        l=list(map(int,input()))
        lst.append(l)
    for i in range(1,n):
        for j in range(10):
            lst[0][j]-=lst[i][j]
            if lst[0][j]<0:
                lst[0][j]=-lst[0][j]
    count=0
    for i in range(10):
        if lst[0][i]==1:
            count+=1
    print(count)
