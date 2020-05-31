t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s=0
    sa,sb=0,0
    for i in range(n):
        sa+=a[i]
        sb+=b[i]
        if a[i]==b[i] and sa==sb:
            s+=a[i]
    print(s)
