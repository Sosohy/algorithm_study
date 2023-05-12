from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
w = []

def bfs(s, cabbage):
    queue = deque([s])
    cabbage[s[0]][s[1]] = 0

    while queue:
        q = queue.popleft()

        for i in range(4):
            nx = q[0] + dx[i]
            ny = q[1] + dy[i]

            if(0 <= nx < n) and (0 <= ny < m) and (cabbage[nx][ny] == 1):
                cabbage[nx][ny] = 0
                queue.append([nx, ny])
                
                
for i in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0]*m for i in range(n)]
    cnt = 0
    
    for j in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    for a in range(n):
        for b in range(m):
            if (cabbage[a][b] == 1):
                cnt += 1
                bfs([a, b], cabbage)
    w.append(cnt)

for i in w:
    print(i)