n, W = map(int, input().split())
items = []
for _ in range(n):
    v, w, m = map(int, input().split())
    k = 1
    # 拆成 1,2,4,... 块
    while m >= k:
        items.append((v * k, w * k))
        m -= k
        k <<= 1
    if m > 0:
        items.append((v * m, w * m))

dp = [0] * (W + 1)
for val, wt in items:
    if wt > W:
        continue
    for j in range(W, wt - 1, -1):
        if dp[j - wt] + val > dp[j]:
            dp[j] = dp[j - wt] + val

print(dp[W])
