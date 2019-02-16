from collections import defaultdict
import operator
for i in range(int(input())):
    s=input()
    d=defaultdict(int)
    s1="abcdefghijklmnopqrstuvwxyz"
    s1=s1.upper()
    for i in s1:
        d[i]=0
    l=[]
    for i in range(1,27):
        if(len(s)%i==0):
            l.append(i)
    for i in s:
        d[i]+=1
    d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    c=0
    fl=[]
    ans=0
    while(c<len(l)):
        count=len(s)//l[c]
        for i in range(l[c]):
            if(d[i][1]<count):
                ans+=count-d[i][1]
        c+=1
        fl.append(ans)
        ans=0
    print(min(fl))






