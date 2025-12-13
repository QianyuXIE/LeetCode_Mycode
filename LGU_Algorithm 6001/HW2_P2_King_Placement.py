N, K = map(int, input().split())

masks = []
count = {}

for mask in range(1<<N):
    if (mask & (mask>>1)) == 0:
        masks.append(mask)
        count[mask] = bin(mask).count('1')

def compatible(a,b):
    if (a & b): return False
    if (a & (b<<1)): return False
    if (a & (b>>1)): return False
    return True

comp = {a:[] for a in masks}
# 记录每一种行排列a所能匹配的所有行排列b
for a in masks:
    for b in masks:
        if compatible(a,b): comp[a].append(b)

# prev[row][total: number of Kings] = number of solutions
prev = [[0]*(K+1) for _ in range(1<<N)]
cur = [[0]*(K+1) for _ in range(1<<N)]

prev[0][0] = 1

for row in range(1,N+1):
    for mask in masks:
        c = count[mask]
        for total in range (c,K+1):
            s = 0
            for pre in comp[mask]:
                s += prev[pre][total - c]
            cur[mask][total] = s
    prev = cur
    cur = [[0]*(K+1) for _ in range(1<<N)]

ans = sum(prev[mask][K] for mask in masks)
print(ans)