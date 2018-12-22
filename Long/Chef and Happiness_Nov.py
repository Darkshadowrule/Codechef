from collections import defaultdict
for  i in range(int(input())):
    n=int(input())
    l1=[0]+list(map(int,input().split()))
    l2=[0]*(n+1)
    for i in range(1,len(l1)):
        l2[i]=l1[l1[i]]
    l3=[(x,y)for x,y in zip(l1,l2)]
    l3=sorted(l3,key=lambda x:x[1])
    f=0
    for i in range(n):
        if(l3[i][1]==l3[i+1][1] and l3[i][0]!=l3[i+1][0]):
            f=1
            break
    if(f):
        print("Truly Happy")
    else:
        print("Poor Chef")
