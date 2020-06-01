# cook your dish here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        count = 0
        n = input()
        for c in n:
            if c == '4':
                count = count + 1
        print(count)

