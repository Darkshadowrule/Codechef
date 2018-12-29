from collections import defaultdict
mod=10**9+7
l2=[[0 for i in range(1001)]for j in range(1001)]
l1=[[0 for i in range(1001)]for j in range(1001)]
l2[0][0]=1
for i in range(1,999):
    l2[i][0]=1
    for j in range(1,i+1):
        l2[i][j]=(l2[i-1][j-1]+l2[i-1][j])%mod
        l1[i][j] += (l2[i][j] + l1[i - 1][j])%mod
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    ans =pow(2,n-1,mod)
    d = defaultdict(int)
    for i in l:
        d[i] += 1
    for i in d:
        ans += l2[d[i]][2]
        ans %= mod
    for i in range(len(l) - 1):
        if (l[i] == l[i + 1]):
            extra = n - i - d[l[i]]
            d[l[i]] -= 1
            start = n - i - 2
            for j in range(1, start + 1):
                if(i<j):
                    break
                if(extra==0):
                    sum1=l1[start][j]
                else:
                    sum1=l1[start][j]-l1[extra-1][j]
                save=(l2[i][j]*sum1)
                if(save==0):
                    break
                ans += save
                ans %= mod
    print(ans)



