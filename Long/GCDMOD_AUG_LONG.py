import math
mod=1000000007
for i in range(int(input())):
    a,b,n=map(int,input().split())
    if(n==1):
        print(math.gcd(a**1+b**1,abs(a-b))%mod)
    elif(a==b):
        d=1
        while(n!=0):
            d*=a
            d%=mod
            n-=1
        print((2*d)%mod)    
    else:
        print(math.gcd(a ** 2 + b ** 2, abs(a - b)) % mod)
