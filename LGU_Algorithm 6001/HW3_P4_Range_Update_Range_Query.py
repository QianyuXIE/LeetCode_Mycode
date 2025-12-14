class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


def range_add(bit1, bit2, l, r, x):
    bit1.add(l, x)
    bit1.add(r + 1, -x)

    bit2.add(l, x * (l - 1))
    bit2.add(r + 1, -x * r)


def prefix_sum(bit1, bit2, i):
    return i * bit1.query(i) - bit2.query(i)


def range_sum(bit1, bit2, l, r):
    return prefix_sum(bit1, bit2, r) - prefix_sum(bit1, bit2, l - 1)


# --- Main ---
n, q = map(int, input().split())
a = list(map(int, input().split()))

bit1 = Fenwick(n)
bit2 = Fenwick(n)

# 初始数组建立：相当于对每个位置单点加
for i in range(1, n + 1):
    range_add(bit1, bit2, i, i, a[i - 1])

out = []
for _ in range(q):
    op = input().split()
    if op[0] == '1':   # range add
        _, l, r, x = op
        l = int(l); r = int(r); x = int(x)
        range_add(bit1, bit2, l, r, x)
    else:             # range sum
        _, l, r = op
        l = int(l); r = int(r)
        out.append(str(range_sum(bit1, bit2, l, r)))

print("\n".join(out))
