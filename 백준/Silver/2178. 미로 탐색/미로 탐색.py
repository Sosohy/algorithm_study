from collections import deque

n, m = map(int, input().split())
mList = []
visited = [[-1]*m for j in range(n)]

for i in range(n):
    mList.append(input())

q = deque()
q.append((0, 0, 1))
visited[0][0] = 1
pos = [(0, 1), (0, -1), (-1, 0), (1, 0)]

while(q):
    x, y, dis = q.popleft()

    for i in range(4):
        nx = x+pos[i][0]
        ny = y+pos[i][1]

        if( 0 <= nx < n and 0 <= ny < m and mList[nx][ny] == '1'):
            if(visited[nx][ny] == -1 or visited[nx][ny] > dis+1):
                visited[nx][ny] = dis+1
                q.append((nx, ny, dis+1))

print(visited[n-1][m-1])
