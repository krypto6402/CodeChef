# cook your dish here
t=int(input())
for i in range(t):
     n,k=map(int,input().split())
     a = list(map(int,input().strip().split()))[:n]
     x=0
     summ=sum(a)
     for x in range(n):
          if a[x]>k:
               a[x]=k
     summ1=sum(a)
     print(summ-summ1)
