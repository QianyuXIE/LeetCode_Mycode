n = int(input())
a = list(map(int, input().split()))

dp = []
ans = 0
dp.append(a[0])

for i in range(1,n):
    dp.append(max(dp[i-1]+a[i], a[i]))

for i in range(n):
    ans = max(ans, dp[i])

print(ans)