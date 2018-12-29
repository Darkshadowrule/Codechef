def digitsum(n,count):
    s = 0
    s1 = 0
    while (n != 0):
        s += n % 10
        n = n // 10
    count+=1
    if (s >= 10):
        return digitsum(s,count)
    else:
        return s,count
def digitsum1(n):
    s=0
    while(n!=0):
        s+=n%10
        n=n//10
    return s
for i in range(int(input())):
    n,d=map(int,input().split())
    l=[]
    l1=[0]*(2**13)
    k=n
    for i in range(10):
        k += d
        if (k % 9 != 0):
            l.append(k % 9)
        else:
            l.append(9)
    min1 = min(set(l))
    c=0
    i=1
    x=2**13
    ans=0
    l1[i]=n
    while(1):
        l1[2*i]=l1[i]+d
        l1[2*i+1]=digitsum1(l1[i])
        if(2*i+1==x-1):
            break
        else:
            i+=1
    ind=0
    for i in range(1,x):
        if(l1[i]==min1):
            ind=i
            break
    while(ind!=0):
        if(ind%2==1):
            ind=(ind-1)//2
            ans+=1
        else:
            ind=(ind-2)//2
            ans+=1
    sum1,cnt=digitsum(n,0)
    l3=[9,99,999,9999,99999,999999,9999999,99999999,999999999]
    if(n==min1):
        print(min1,0)
    elif(n in l3 and d in l3):
        print("9 2")
    elif(sum1==min1):
        print(min1,cnt)
    else:
        print(min1,ans)

















