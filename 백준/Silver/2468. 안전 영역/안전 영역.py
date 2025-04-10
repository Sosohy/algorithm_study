from collections import deque

n = int(input())
nList = []
mIdx = 0
ans = 1

for i in range(n):
    tmp = list(map(int, input().split()))
    nList.append(tmp)
    mIdx = max(mIdx, max(tmp))
        
def bfs(r, c, idx):
    q = deque([(r,c)])
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while(q):
        x, y = q.popleft()

        for s in range(4):
            nx = x+pos[s][0]
            ny = y+pos[s][1]
            if(0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0):
                if(nList[nx][ny] > idx):
                    q.append([nx, ny])
                    visited[nx][ny] = 1

for k in range(1, mIdx):
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if(nList[i][j] > k and visited[i][j] == 0):
                visited[i][j] = 1
                bfs(i, j, k)
                cnt += 1

    ans = max(ans, cnt)

print(ans)
