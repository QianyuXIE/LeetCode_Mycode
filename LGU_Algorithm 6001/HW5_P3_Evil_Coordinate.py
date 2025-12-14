ORDERS = [
    "UDLR","UDRL","ULDR","ULRD","URDL","URLD",
    "DULR","DURL","DLUR","DLRU","DRUL","DRLU",
    "LUDR","LURD","LDUR","LDRU","LRUD","LRDU",
    "RUDL","RULD","RDUL","RDLU","RLUD","RLDU",
]

def main():
    T = int(input().strip())
    for _ in range(T):
        mx, my = map(int, input().split())
        s = input().strip()

        # 起点就踩雷：无法避免
        if mx == 0 and my == 0:
            print("Impossible")
            continue

        cntU = cntD = cntL = cntR = 0
        for ch in s:
            if ch == 'U':
                cntU += 1
            elif ch == 'D':
                cntD += 1
            elif ch == 'L':
                cntL += 1
            else:
                cntR += 1

        cnt = {'U': cntU, 'D': cntD, 'L': cntL, 'R': cntR}

        ans = None

        # 检查每一种块顺序
        for order in ORDERS:
            x = 0
            y = 0
            ok = True

            for ch in order:
                c = cnt[ch]
                if c == 0:
                    continue

                if ch == 'U':
                    # 从 (x,y) 走到 (x, y+c)，中间经过 y+1..y+c
                    if mx == x and (y < my <= y + c):
                        ok = False
                        break
                    y += c
                elif ch == 'D':
                    # 经过 y-1..y-c
                    if mx == x and (y - c <= my < y):
                        ok = False
                        break
                    y -= c
                elif ch == 'R':
                    # 经过 x+1..x+c
                    if my == y and (x < mx <= x + c):
                        ok = False
                        break
                    x += c
                else:  # 'L'
                    # 经过 x-1..x-c
                    if my == y and (x - c <= mx < x):
                        ok = False
                        break
                    x -= c

            if ok:
                # 构造答案：同字符聚成块
                ans = ""
                for ch in order:
                    if cnt[ch]:
                        ans += ch * cnt[ch]
                break

        print(ans if ans is not None else "Impossible")

if __name__ == "__main__":
    main()