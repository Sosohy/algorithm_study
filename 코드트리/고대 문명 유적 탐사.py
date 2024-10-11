from collections import deque
K, M = map(int, input().split())
mapList = [list(map(int, input().split())) for i in range(5)]
numList = deque(list(map(int, input().split())))
answer = []

def rotate(sy, sx, d):
    board = [x[:] for x in mapList]

    for _ in range(d+1):
        tmp = board[sy + 0][sx + 2]
        board[sy + 0][sx + 2] = board[sy + 0][sx + 0]
        board[sy + 0][sx + 0] = board[sy + 2][sx + 0]
        board[sy + 2][sx + 0] = board[sy + 2][sx + 2]
        board[sy + 2][sx + 2] = tmp
        tmp = board[sy + 1][sx + 2]
        board[sy + 1][sx + 2] = board[sy + 0][sx + 1]
        board[sy + 0][sx + 1] = board[sy + 1][sx + 0]
        board[sy + 1][sx + 0] = board[sy + 2][sx + 1]
        board[sy + 2][sx + 1] = tmp

    return board

def inRange(x, y):
        return (0 <= x < 5) and (0<= y < 5)

def getCnt(arr, clear):
    visited = [[False]*5 for _ in range(5)]
    score = 0
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

    for i in range(5):
        for j in range(5):
            if(not visited[i][j]):
                q, trace = deque([(i, j)]), deque([(i, j)])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x+pos[k][0]
                        ny = y+pos[k][1]
                        if(inRange(nx, ny) and not visited[nx][ny] and arr[x][y] == arr[nx][ny]):
                            q.append((nx, ny))
                            trace.append((nx, ny))
                            visited[nx][ny] = True

                if(len(trace) >= 3):
                    score += len(trace)
                    if(clear):
                        while trace:
                            t = trace.popleft()
                            arr[t[0]][t[1]] = 0
                        
    return score

def fillList():
    for c in range(5):
        for r in range(4, -1, -1):
            if(mapList[r][c] == 0):
                mapList[r][c] = numList.popleft()
                numList.append(mapList[r][c])

for i in range(K):
    maxCnt = 0
    tmpList = None
    for deg in range(3): # 90, 180, 270
        for c in range(3):
            for r in range(3):
                rotated = rotate(r, c, deg) # 회전
                cnt = getCnt(rotated, False) # 유물 수
                if(maxCnt < cnt): # 최대값 비교
                    maxCnt = cnt
                    tmpList = rotated

    if maxCnt == 0:
        break

    # 최대값 배열로 유물 획득, 연쇄 획득
    cnt = 0
    mapList = tmpList
    while(True):
        tmp = getCnt(mapList, True)
        if(tmp == 0):
            break
        cnt += tmp

        fillList()
    
    answer.append(cnt)

print(" ".join(list(map(str, answer))))
