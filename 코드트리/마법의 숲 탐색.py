from collections import deque

r, c, k = map(int, input().split())
forest = [[0]*c for i in range(r+3)]
exit = [[False]*c for i in range(r+3)]
pos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0

def canDown(y, x):
    flag = (0 <= x-1 and x+1 < c and y+1 < r+3)
    flag = flag and (forest[y][x-1] == 0)
    flag = flag and (forest[y][x+1] == 0)
    flag = flag and (forest[y+1][x] == 0)
    return flag

def canLeft(y, x):
    flag = (0 <= x-1 and x+1 < c and y+1 < r+3)
    flag = flag and (forest[y-1][x-1] == 0)
    flag = flag and (forest[y][x] == 0)
    flag = flag and (forest[y][x-1] == 0)
    flag = flag and (forest[y+1][x] == 0)
    return flag

def canRight(y, x):
    flag = (0 <= x-1 and x+1 < c and y+1 < r+3)
    flag = flag and (forest[y-1][x+1] == 0)
    flag = flag and (forest[y][x] == 0)
    flag = flag and (forest[y][x+1] == 0)
    flag = flag and (forest[y+1][x] == 0)
    return flag

def inRange(y, x):
    return 3 <= y < r+3 and 0 <= x < c

def bfs(y, x):
    result = y
    q = deque([(y, x)])
    visited = [[False]*c for _ in range(r+3)]
    visited[y][x] = True
    while q:
        ny, nx = q.popleft()
        for j in range(4):
            dy, dx = ny+pos[j][0], nx+pos[j][1]
            if(inRange(dy, dx) and not visited[dy][dx] and (forest[dy][dx] == forest[ny][nx] or (forest[dy][dx] != 0 and exit[ny][nx]))):
                q.append((dy, dx))
                visited[dy][dx] = True
                result = max(result, dy)
    return result

def move(y, x, d, idx): 
    if(canDown(y+1, x)):
        move(y+1, x, d, idx)
    elif(canLeft(y+1, x-1)):
        move(y+1, x-1, (d+3)%4, idx)
    elif(canRight(y+1, x+1)):
        move(y+1, x+1, (d+1)%4, idx)
    else:
        if not inRange(y-1, x-1) or not inRange(y+1, x+1):
            for a in range(r+3):
                for b in range(c):
                    forest[a][b] = 0
                    exit[a][b] = False
        else:
            forest[y][x] = idx
            for i in range(4):
                ny, nx = y+pos[i][0], x+pos[i][1]
                forest[ny][nx] = idx
            exit[y+pos[d][0]][x+pos[d][1]] = True
            global answer
            answer += bfs(y, x) - 2


for id in range(1, k+1):
    x, d = map(int, input().split()) # 북 동 남 서
    move(1, x-1, d, id)
    
print(answer)
