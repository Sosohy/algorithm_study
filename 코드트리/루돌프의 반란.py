N, M, P, C, D = map(int, input().split())

mapList = [[-1]*(N+1) for _ in range(N+1)]
rudolph = tuple(map(int, input().split()))
santa = {}
isAlive = [0]*(P+1)
score = [0]*(P+1)
pos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

mapList[rudolph[0]][rudolph[1]] = 0
for i in range(P):
    idx, r, c = map(int, input().split())
    santa[idx] = (r, c)
    mapList[r][c] = idx

def inRange(y, x):
    return (1 <= y < N+1) and (1 <= x < N+1)

def calDist(d1, d2):
    return (d1[0]-d2[0])**2 + (d1[1]-d2[1])**2

def findRudolph(idx):
    s = santa[idx]

    minDist = calDist(s, rudolph)
    minPos = (s[0], s[1])
    minIdx = -1

    for j in range(4):
        ny, nx = s[0]+pos[j][0], s[1]+pos[j][1]
        dist = calDist((ny, nx), rudolph)

        if(inRange(ny, nx) and mapList[ny][nx] < 1 and dist < minDist):
            minDist = dist
            minPos = (ny, nx)
            minIdx = j
    
    mapList[santa[idx][0]][santa[idx][1]] = -1
    santa[idx] = minPos
    
    # 충돌 확인
    if(mapList[santa[idx][0]][santa[idx][1]] == 0):
        score[idx] += D

        # D칸 반대로 밀려나기
        sy, sx = santa[idx][0] + -pos[minIdx][0]*D, santa[idx][1] + -pos[minIdx][1]*D
        santa[idx] = (sy, sx)
        isAlive[idx] = 2
            
        # 상호작용
        while(True):
            if(not inRange(sy, sx)):
                isAlive[idx] = -1
                break

            if(mapList[sy][sx] < 0):
                mapList[sy][sx] = idx
                break
            else:
                tmp = mapList[sy][sx]
                mapList[sy][sx] = idx
                idx = tmp
                sy += -pos[minIdx][0]
                sx += -pos[minIdx][1]
                santa[idx] = (sy, sx)
    else:
        mapList[santa[idx][0]][santa[idx][1]] = idx

def findNearSanta(y, x):
    global rudolph
    minDist = None
    minPos = None

    # 가까운 산타 찾기
    for r in range(1, N+1):
        for c in range(1, N+1):
            if(mapList[r][c] > 0 and isAlive[mapList[r][c]] >= 0):
                dist = calDist((y, x), (r, c))
                if(not minDist or minDist >= dist):
                    minDist = dist
                    minPos = (r, c)
                    
    ny, nx = 0, 0
    if(not minPos):
        return False
    else: # 찾은 산타로 루돌프 방향 찾기
        if(minPos[0] > y):
            ny += 1
        elif(minPos[0] < y):
            ny -= 1
        
        if(minPos[1] > x):
            nx += 1
        elif(minPos[1] < x):
            nx -= 1
        
        mapList[y][x] = -1
        rudolph = (y+ny, x+nx)
    
    # 충돌 확인
    if(mapList[rudolph[0]][rudolph[1]] > 0):
        idx = mapList[rudolph[0]][rudolph[1]]
        score[idx] += C
        mapList[rudolph[0]][rudolph[1]] = 0

        # C칸 밀려나기
        sy, sx = santa[idx][0] + ny*C, santa[idx][1] + nx*C
        santa[idx] = (sy, sx)
        isAlive[idx] = 2
            
        # 상호작용
        while(True):
            if(not inRange(sy, sx)):
                isAlive[idx] = -1
                break

            if(mapList[sy][sx] < 0):
                mapList[sy][sx] = idx
                break
            else:
                tmp = mapList[sy][sx]
                mapList[sy][sx] = idx
                idx = tmp
                sy += ny
                sx += nx
                santa[idx] = (sy, sx)
    else:
        mapList[rudolph[0]][rudolph[1]] = 0


for m in range(M):

    # 루돌프 턴
    # 가장 가까운 산타 찾기, 충돌 체크
    findNearSanta(rudolph[0], rudolph[1])

    # 산타 턴
    for i in range(1, P+1):
        if(isAlive[i] == 0): # 게임 가능한 산타
            findRudolph(i) # 루돌프 쪽으로 이동, 충돌 체크

    # 턴 추가 처리
    for i in range(1, P+1): 
        if(isAlive[i] >= 0): # 살아남은 산타들 1점 추가 부여
            score[i] += 1
        if(isAlive[i] > 0): # 기절한 경우 턴 --
            isAlive[i] -= 1

sc = " ".join(map(str, score[1:]))
print(sc)
