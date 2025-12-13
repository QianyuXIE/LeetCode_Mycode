from array import array

def main():
    N, M, S = map(int, input().split())

    # --- 用前向星存图：省内存，适合 N=5e5 ---
    E = 2 * (N - 1)
    head = array('i', [-1]) * (N + 1)
    to   = array('i', [0])  * E
    nxt  = array('i', [0])  * E

    idx = 0
    for _ in range(N - 1):
        x, y = map(int, input().split())
        to[idx] = y
        nxt[idx] = head[x]
        head[x] = idx
        idx += 1

        to[idx] = x
        nxt[idx] = head[y]
        head[y] = idx
        idx += 1

    # --- 1) DFS/BFS 求 depth 和 up[0] (父亲) ---
    parent0 = array('i', [0]) * (N + 1)
    depth   = array('i', [0]) * (N + 1)

    stack = [S]
    parent0[S] = 0
    depth[S] = 0

    while stack:
        u = stack.pop()
        e = head[u]
        while e != -1:
            v = to[e]
            if v != parent0[u]:
                parent0[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)
            e = nxt[e]

    # --- 2) 倍增表 up[j][v] ---
    LOG = (N).bit_length()
    up = [parent0]
    for j in range(1, LOG):
        prev = up[j - 1]
        cur = array('i', [0]) * (N + 1)
        for v in range(1, N + 1):
            cur[v] = prev[prev[v]]
        up.append(cur)

    def lca(a: int, b: int) -> int:
        if depth[a] < depth[b]:
            a, b = b, a

        # 把 a 抬到和 b 同深度
        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                a = up[bit][a]
            diff >>= 1
            bit += 1

        if a == b:
            return a

        # 从大到小一起跳
        for j in range(LOG - 1, -1, -1):
            if up[j][a] != up[j][b]:
                a = up[j][a]
                b = up[j][b]

        return up[0][a]

    # --- 3) 回答查询 ---
    out = []
    for _ in range(M):
        a, b = map(int, input().split())
        out.append(str(lca(a, b)))
    print("\n".join(out))

if __name__ == "__main__":
    main()