N = int(input())
nList = list(map(int, input().split()))
M = int(input())

ans = 0
s, e, mid = 1, max(nList), 0

while(s <= e):
    mid = (s+e)//2

    cnt = 0
    for i in nList:
        cnt += min(i, mid)
    
    if(cnt == M):
        ans = mid
        break
    if(cnt < M):
        s = mid+1
        ans = mid
    else:
        e = mid-1

print(ans)