l=list(map(int,input().split()))
l=l[1:]
l1=[0]*30
l2=[0]*30
l1[0]=1
l2[0]=2
for i in range(1,30):
    l1[i]=2*l1[i-1]+(-1)**i
    l2[i]=2**(i+1)
for i in range(len(l)):
    print(l1[l[i]-1],l2[l[i]-1],end=" ")
