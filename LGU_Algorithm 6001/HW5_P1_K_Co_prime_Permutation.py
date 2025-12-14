def main():
    n, k = map(int, input().split())

    if k == 0:
        print(-1)
        return

    if k == 1:
        # 1..n
        perm = list(range(1, n + 1))
    else:
        # k, 1..k-1, k+1..n
        perm = [k] + list(range(1, k)) + list(range(k + 1, n + 1))
        
    print(" ".join(map(str, perm)))

if __name__ == "__main__":
    main()
