# cook your dish here
t = int(input())
while (t):
    t = t-1
    n = int(input())
    a = list(map(int,input().split()))
    bal = 0
    c = 0
    if a[0] != 5:
        print('NO')
    if a[0] == 5:
        bal = 5
        c = c+1
        for i in range (1,n):
            if bal-(a[i]-5) >= 0:
                c = c+1
                bal = bal+5
            else:
                break
        if c == n:
            print('YES')
        else:
            print('NO')
