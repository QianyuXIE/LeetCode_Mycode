def Msort(arr, n):
    if n <= 1:
        return arr, 0
    
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    Msorted_left, count_l = Msort(left, mid)
    Msorted_right, count_r = Msort(right, n-mid)

    count = count_l + count_r

    merged, cross_count = merge(Msorted_left, Msorted_right)
    count += cross_count

    return merged, count

def merge(left, right):
    i = 0
    j = 0
    tmp = []
    count = 0
    len_l = len(left)
    len_r = len(right)

    while(i<len_l and j<len_r):
        if left[i]<right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
            count += len_l - i

    while(i<len_l):
        tmp.append(left[i])
        i += 1

    while(j<len_r):
        tmp.append(right[j])
        j += 1

    return tmp, count

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr, count = Msort(arr, n)
    print(count)