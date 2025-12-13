class Node:
    def __init__(self, sum=0, lmax=-10**18, rmax=-10**18, tmax=-10**18):
        self.sum = sum
        self.lmax = lmax
        self.rmax = rmax
        self.tmax = tmax

def merge(L, R):
    res = Node()
    res.sum = L.sum + R.sum
    res.lmax = max(L.lmax, L.sum + R.lmax)
    res.rmax = max(R.rmax, R.sum + L.rmax)
    res.tmax = max(max(L.tmax, R.tmax), L.rmax + R.lmax)
    return res

def build(idx, l, r):
    if l == r:
        x = A[l]
        seg[idx] = Node(x, x, x, x)
        return
    mid = (l + r) >> 1
    build(idx*2, l, mid)
    build(idx*2+1, mid+1, r)
    seg[idx] = merge(seg[idx*2], seg[idx*2+1])

def query(idx, l, r, ql, qr):
    if ql <= l and r <= qr:
        return seg[idx]
    mid = (l + r) >> 1
    if qr <= mid:
        return query(idx*2, l, mid, ql, qr)
    if ql > mid:
        return query(idx*2+1, mid+1, r, ql, qr)
    left = query(idx*2, l, mid, ql, qr)
    right = query(idx*2+1, mid+1, r, ql, qr)
    return merge(left, right)


N = int(input())
A = [0] + list(map(int, input().split()))
seg = [Node() for _ in range(4 * N)]

build(1, 1, N)

M = int(input())
out = []
for _ in range(M):
    x, y = map(int, input().split())
    ans = query(1, 1, N, x, y).tmax
    out.append(str(ans))

print("\n".join(out))
