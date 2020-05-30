import math
t=int(input())
for p in range(t):
     n,a,k=map(int,input().split())
     x=2*(180*n-360-a*n)(k-1)+(a*n(n-1))
     y=n*(n-1)
     ans=math.gcd(x,y)
     x=x//ans
     y=y//ans
     print(x,y)
