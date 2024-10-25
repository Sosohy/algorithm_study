N, M = map(int, input().split())
mList = [int(input()) for _ in range(N)]

s, e, mid = max(mList), sum(mList), 0

answer = 0

while(s <= e):
    mid = (s+e)//2

    money = 0
    cnt = 1
    for m in mList:
        if(money+m <= mid):
            money += m
        else:
            cnt += 1
            money = m
    
    if(cnt > M):
        s = mid+1
    else:
        e = mid-1
        answer = mid

print(answer)

