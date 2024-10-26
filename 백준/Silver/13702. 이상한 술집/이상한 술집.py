N, K = map(int, input().split())
nList = [int(input()) for _ in range(N)]

s, e, mid = 1, sum(nList), 0

def cal(m):
    if(m == 0):
        return False
    
    cnt = 0
    for i in nList:
        cnt += i//m
    
    return cnt >= K

ans = 0
while(s <= e):
    mid = (s+e)//2

    if(cal(mid)):
        ans = mid
        s = mid+1
    else:
        e = mid-1

print(ans)