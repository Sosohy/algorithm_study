n, m = map(int, input().split())
mapList = []
pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
maxWidth = 0
num = 0

for i in range(n):
    mapList.append(input().split())

def bfs(x ,y):
    q = [(x, y)]
    mapList[x][y] = "-1"
    cnt = 1

    while(q):
        x, y = q.pop(0)
        for i in pos:
            nx = x + i[0]
            ny = y + i[1]
            if(0 <= nx < n and 0 <= ny < m and mapList[nx][ny] == "1"):
                cnt += 1
                mapList[nx][ny] = "-1"
                q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(m):
        if(mapList[i][j] == "1"):
            num += 1
            width = bfs(i, j)
            maxWidth = max(maxWidth, width)

print(num)
print(maxWidth)
