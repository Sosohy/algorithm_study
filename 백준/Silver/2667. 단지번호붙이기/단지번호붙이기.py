from collections import deque

n = int(input())
comp = [input() for i in range(n)]
visited = [[-1]*n for i in range(n)]
num = []

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    pos = [(1, 0),(-1, 0), (0, 1), (0, -1)]
    cnt = 1

    while(q):
        x, y = q.popleft()

        for k in range(4):
            nx = x+pos[k][0]
            ny = y+pos[k][1]

            if(0 <= nx < n and 0 <= ny < n and comp[nx][ny] == '1' and visited[nx][ny] == -1):
                visited[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    
    return cnt

for i in range(n):
    for j in range(n):
        if(comp[i][j] == '1' and visited[i][j] == -1):
            num.append(bfs(i, j))

print(len(num))

num.sort()
for i in range(len(num)):
    print(num[i])            