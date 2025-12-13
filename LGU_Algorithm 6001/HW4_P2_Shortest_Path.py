import heapq

def main():
    n, m, s, t = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))  # 无向图两边都加

    INF = 10**30
    dist = [INF] * (n + 1)
    dist[s] = 0

    pq = [(0, s)]  # (当前距离, 节点)

    while pq:
        d, u = heapq.heappop(pq)

        # 这是“过期状态”：堆里可能有旧的更大距离，需要丢掉
        if d != dist[u]:
            continue

        # 已经以最小距离弹出 t，最短路定了，可以提前结束
        if u == t:
            break

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    print(dist[t])

if __name__ == "__main__":
    main()
