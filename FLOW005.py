# cook your dish here
t = int(input())
money = [1,2,5,10,50,100]
for i in range(t):
    count = 0
    n = int(input())
    i = -1
    while n > 0:
        count = count + n // money[i]
        n = n % money[i]
        i = i-1
    print(count)
