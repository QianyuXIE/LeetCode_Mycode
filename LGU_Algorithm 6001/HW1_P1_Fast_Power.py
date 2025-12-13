def compute_exp(x, k):
    mod = 998244353
    if k == 0:
        return 1
    if k % 2 == 0:
        half = compute_exp(x, k/2)
        return (half * half) % mod
    else:
        half = compute_exp(x, (k-1)/2)
        return (half * half * x) % mod

x, k = map(int, input().split())
print(compute_exp(x, k))    