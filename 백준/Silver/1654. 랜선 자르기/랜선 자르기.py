K, N = map(int, input().split())
kList = [int(input()) for _ in range(K)]

s, e, mid = 1, max(kList), 0
ans = 0

while(s <= e):
    mid = (s+e)//2

    cnt = 0
    if(mid > 0):
        for i in kList:
            cnt += (i//mid)
    if(cnt >= N):
        ans = mid
        s = mid+1

    if(cnt < N):
        e = mid-1

print(ans)
    