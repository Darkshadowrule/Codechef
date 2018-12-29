def check(l4,m,can,k):
    while(True):
        #print("ko")
        try:
            if(can>=l4[k-1][2]):
                break
            temp = l4[k - 1][0] - can // l4[k - 1][1]
            m -= temp
            k-=1
        except:
            break
    if(m>=0):
        return True
    else:
        return False
n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
if (sum(l1) <= m):
    print("0")
elif(n==1):
    ans=l1[0]-m
    print(ans*l2[0])
else:
    l3 = [(l1[i] * l2[i]) for i in range(n)]
    l4 = [(x, y, z) for x, y, z in zip(l1, l2, l3)]
    l4 = sorted(l4, key=lambda x: x[2])
    low=1
    high=l4[n-1][2]
    while(True):
        if(low==high-1):
            break
        mid=low+(high-low)//2
        if(check(l4,m,mid,n)):
            high=mid
        else:
            low=mid
    if(check(l4,m,high,n)):
        ans=high
    else:
        ans=low
    print(ans)
