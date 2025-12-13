from collections import deque

N, K = map(int, input().split())
E = [int(input()) for _ in range(N)]

prefix = [0] * (N + 1)
for r in range(1, N + 1):
    prefix[r] = prefix[r - 1] + E[r - 1]

dp = [0] * (N + 1)

# Maintain A[j] = dp[j] - prefix[j+1] in deque in decreasing order.
dq = deque()
dq.append(-1)

for r in range(1, N + 1):
    # remove j out of window, need j >= r - K - 1
    while dq and dq[0] < r - K - 1:
        dq.popleft()

    j = dq[0]
    best_A = (dp[j] - prefix[j + 1]) if j >= 0 else 0
    candidate = prefix[r] + best_A
    dp[r] = max(dp[r - 1], candidate)

    j_new = r - 1
    A_new = dp[j_new] - prefix[j_new + 1]
    
    while dq:
        last = dq[-1]
        last_A = (dp[last] - prefix[last + 1]) if last >= 0 else 0
        if last_A <= A_new:
            dq.pop()
        else:
            break
    dq.append(j_new)

print(dp[N])