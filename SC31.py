t=int(input())
for x in range(t):
     n=int(input())
     a=[]
     for i in range(n):
          ele=list(map(int,input()))
          a.append(ele)
     for i in range(1,n):
          for j in range(10):
               a[0][j]=a[0][j]-a[i][j]
               if a[0][j]<0:
                    a[0][j]=(-1)*a[0][j]
     p=0
     for i in range(10):
          p+=a[0][i]

     print(p)
