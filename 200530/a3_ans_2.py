n=int(input())
a = list(map(int,input().split()))
i=0
b=0
while i<=n:
    b+=a[i]
    i+=1
i=0
x=1
ans=0
while i<=n:
    if a[i] <=x:
        if x<=b:
            ans+=x
            x=(x-a[i])*2
        else:
            ans+=b
            x = b
        b-=a[i]
    else:
        ans=-1
        break
    i+=1
print(ans)
