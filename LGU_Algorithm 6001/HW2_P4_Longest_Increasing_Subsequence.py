n = int(input())
nums = list(map(int, input().split()))

tail = []

for x in nums:
    l, r = 0, len(tail)
    while l < r:
        mid = (l + r) // 2
        if tail[mid] < x:
            l = mid + 1
        else:
            r = mid
    # l 是第一个 >= x 的位置
    if l == len(tail):
        tail.append(x)
    else:
        tail[l] = x

print(len(tail))
