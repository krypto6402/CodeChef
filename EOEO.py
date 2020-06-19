t = int(input())
for i in range(t):
    ts = int(input())
    c=0
    ans=0
    tts=ts
    while(ts%2==0):
        ts=ts//2
        c+=1
    js = pow(2,c+1)
    if(js<=tts):
        ans = tts//js
    print(ans)
