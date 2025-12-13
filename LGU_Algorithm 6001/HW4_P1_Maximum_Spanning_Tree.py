class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        # 路径压缩：把“找祖宗”的路压扁，越用越快
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # 同一集合，加这条边会成环

        # 按秩合并：矮树挂高树上，保持结构更扁
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    # 1) 边按权重从小到大排序
    edges.sort()

    dsu = DSU(n)
    total = 0
    used = 0

    # 2) 从最小边开始尝试加入生成树
    for w, u, v in edges:
        if dsu.union(u, v):   # 能合并两个不同连通块 -> 这条边可用
            total += w
            used += 1
            if used == n - 1:  # 生成树边数够了（n个点的树恰好n-1条边）
                break

    print(total)


if __name__ == "__main__":
    main()