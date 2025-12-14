def read_n_ints(n):
    arr = []
    while len(arr) < n:
        arr.extend(map(int, input().split()))
    return arr

def main():
    n, k, m, c, d = map(int, input().split())
    a = read_n_ints(n)

    P = n - m + 1          # 窗口起点 p 的数量（p=0..P-1）
    mm1 = m - 1

    mx = 0
    for v in a:
        if v > mx:
            mx = v

    # 上界：最多把某个元素加到 a[i] + c + d*(m-1)
    hi = mx + c + d * (m - 1)
    lo = 0

    def feasible(X):
        # base: 不操作也已经 >=X 的数量
        base = 0
        for v in a:
            if v >= X:
                base += 1
        if base >= k:
            return True

        need = k - base  # 还需要抬起来多少个 <X 的元素

        # 差分数组：对每个可行起点区间 [L,R] 做 diff[L]+=1, diff[R+1]-=1
        diff = [0] * (P + 2)

        if d == 0:
            # 增量恒为 c
            for i in range(n):
                if a[i] >= X:
                    continue
                if a[i] + c >= X:
                    L = i - mm1
                    R = i
                    if L < 0:
                        L = 0
                    if R > P - 1:
                        R = P - 1
                    if L <= R:
                        diff[L] += 1
                        diff[R + 1] -= 1
        else:
            for i in range(n):
                if a[i] >= X:
                    continue

                # 需要 d*(i-p) >= X - a[i] - c
                need_inc = X - a[i] - c
                if need_inc <= 0:
                    r = 0
                else:
                    r = (need_inc + d - 1) // d  # ceil(need_inc / d)

                if r > mm1:
                    continue  # 即使在窗口最右端也不够抬到 X

                # p 必须满足：
                # 1) 覆盖 i： i-(m-1) <= p <= i
                # 2) i-p >= r  => p <= i-r
                L = i - mm1
                R = i - r

                if L < 0:
                    L = 0
                if R > P - 1:
                    R = P - 1
                if L <= R:
                    diff[L] += 1
                    diff[R + 1] -= 1

        cur = 0
        best = 0
        for p in range(P):
            cur += diff[p]
            if cur > best:
                best = cur
                if best >= need:
                    return True
        return False

    # 二分最大可行 X
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid - 1

    print(lo)

if __name__ == "__main__":
    main()
