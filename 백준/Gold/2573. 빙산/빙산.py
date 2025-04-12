from collections import deque

N, M = map(int, input().split())
nList = [list(map(int, input().split())) for i in range(N)]
pos = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def iceM():
    tmp = [[0]*M for i in range(N)]

    for i in range(N):
        for j in range(M):
            if(nList[i][j] > 0):
                cnt = 0
                for p in pos:
                    nx, ny = i+p[0], j+p[1]
                    if(nList[nx][ny] == 0):
                        cnt += 1
                tmp[i][j] = cnt

    for i in range(N):
        for j in range(M):
            if(nList[i][j] > 0):
                nList[i][j] = max(0, nList[i][j]-tmp[i][j])

def bfs(x, y):
    q = deque([(x, y)])
    
    while(q):
        x1, y1 = q.popleft()

        for p in pos:
            nx, ny = x1+p[0], y1+p[1]

            if(0<=nx<N and 0<=ny<M and visited[nx][ny] == 0):
                if(nList[nx][ny] > 0):
                    q.append((nx, ny))
                    visited[nx][ny] = 1
year = 0
while(True):
    visited = [[0]*M for i in range(N)]
    ice = 0
    for i in range(N):
        for j in range(M):
            if(nList[i][j] > 0 and visited[i][j] == 0):
                visited[i][j] = 1
                bfs(i, j)
                ice += 1

    if(ice == 0 or ice >= 2):
        break
    else:
        iceM()
        year += 1

if(ice == 0): print(0)
else: print(year)