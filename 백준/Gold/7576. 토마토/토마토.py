from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        s = queue.popleft()

        for i in range(4):
            nx = dx[i] + s[0]
            ny = dy[i] + s[1]

            if (0 <= nx < n) and (0 <= ny < m) and box[nx][ny] == 0:
                box[nx][ny] = box[s[0]][s[1]] + 1
                queue.append([nx, ny])

bfs()

ans = max(map(max, box)) -1
for i in box:
    if(i.count(0) != 0):
        ans = -1
        break;

print(ans)