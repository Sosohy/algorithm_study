from collections import deque

m, n, h = map(int, input().split()) # 가로, 세로, 높이
tomato = []

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    tomato.append(tmp)

# 익은 토마토 인접한 곳 처리
def bfs():
    q = deque()
    pos = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if(tomato[i][j][k] == 1):
                    q.append((i, j, k))

    while(q):
        hh, x, y = q.popleft()

        for i in range(6):
            nh = hh+pos[i][0]
            nx = x+pos[i][1]
            ny = y+pos[i][2]
            
            if(0 <= nx < n and 0 <= ny < m and 0 <= nh < h and tomato[nh][nx][ny] == 0):
                tomato[nh][nx][ny] = tomato[hh][x][y]+1
                q.append((nh, nx, ny))
                
bfs()

# 익지않은 토마토 있는지 확인
mr = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(tomato[i][j][k] == 0):
                print(-1)
                exit(0)       
            mr = max(mr, tomato[i][j][k])

print(mr-1)

