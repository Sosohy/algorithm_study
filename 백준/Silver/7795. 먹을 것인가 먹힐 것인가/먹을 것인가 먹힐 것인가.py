T = int(input())

def lowerIdx(b, idx, r, a):
    res = -1
    while idx <= r:
        mid = (idx + r) // 2
        if b[mid] < a:
            res = mid
            idx = mid + 1
        else: r = mid - 1
    return res

for i in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    cnt = 0
    for a in A:
        cnt += lowerIdx(B, 0, m-1, a)+1
    
    print(cnt)
