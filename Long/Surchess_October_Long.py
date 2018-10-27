n, m = map(int, input().split())
dp = [[0 for x in range(m + 1)] for y in range(n + 1)]
l1 = [[0 for x in range(m)] for y in range(n)]
l2 = [[0 for x in range(m)] for y in range(n)]
for ii in range(n):
    for jj in range(m):
        if ((ii + jj) % 2 == 0):
            l2[ii][jj] = 1
        else:
            l2[ii][jj] = 0
for i in range(n):
    s = input()
    for j in range(m):
        l1[i][j] = int(s[j])
l = [0] * min(n, m)
sq = min(n, m)
l3 = [0] * (sq)
for i in range(n):
    s = 0
    for j in range(m):
        if (l1[i][j] != l2[i][j]):
            s += 1
            dp[i + 1][j + 1] = s
        else:
            dp[i + 1][j + 1] = s
# print(dp)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j]
# print(dp)
for no in range(sq, 1, -1):
    mymin = 1000000
    for i in range(n):
        for j in range(m):
            if (i + no <= n and j + no <= m):
                ans = dp[i + no][j + no] - dp[i][j + no] - dp[i + no][j] + dp[i][j]
                ans = min(ans, no * no - ans)
                if (ans < mymin):
                    mymin = ans
    l3[no - 1] = mymin
    if(mymin==0):
        break
#print(l3)
q=int(input())
lq = list(map(int, input().split()))
for i in lq:
    if (i > (sq * sq // 2)):
        print(sq)
    else:
        for j in range(len(l3) - 1, -1, -1):
            if (l3[j] <= i):
                print(j + 1)
                break


