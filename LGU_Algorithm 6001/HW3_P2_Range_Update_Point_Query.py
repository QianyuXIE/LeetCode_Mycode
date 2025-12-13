n, q = map(int, input().split())
a = list(map(int, input().split()))

# Fenwick tree
bit = [0] * (n + 2)

def add(i, x):
    while i <= n:
        bit[i] += x
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

out = []
for _ in range(q):
    op = input().split()
    if op[0] == '1':
        l = int(op[1])
        r = int(op[2])
        x = int(op[3])
        add(l, x)
        add(r + 1, -x)
    else:
        i = int(op[1])
        out.append(str(a[i-1] + query(i)))

print("\n".join(out))
