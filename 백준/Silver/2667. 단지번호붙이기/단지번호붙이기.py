from collections import deque

n = int(input())
town = [list(map(int, input())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

com = []
c = 1

def bfs(s):
    queue = deque([s])
    town[s[0]][s[1]] = 0
    cnt = 1

    while queue:
        q = queue.popleft()
        
        for i in range(4):
            nx = q[0] + dx[i]
            ny = q[1] + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and town[nx][ny] == 1:
                town[nx][ny] = 3
                cnt += 1
                queue.append([nx, ny])

    return cnt

for i in range(n):
    for j in range(n):
        if (town[i][j] == 1):
            com.append(bfs([i, j]))

print(len(com))
for i in sorted(com):
    print(i)