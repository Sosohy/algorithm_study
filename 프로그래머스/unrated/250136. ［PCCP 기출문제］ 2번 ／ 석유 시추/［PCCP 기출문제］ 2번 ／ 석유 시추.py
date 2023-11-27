from collections import deque
def solution(land):
    answer = 0
    dic = {}
    landDic = {}
    cnt = 2
    
    def bfs(n, m):
        queue = deque()
        pos = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        oil = 1
        
        if m not in landDic:
            landDic[m] = set()
        landDic[m].add(cnt)
        land[n][m] = cnt
        queue.append((n, m))
        
        while(queue):
            x, y = queue.popleft()

            for k in range(4):
                nx = x+pos[k][0]
                ny = y+pos[k][1]

                if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny] == 1:
                    if ny not in landDic:
                        landDic[ny] = set()
                    landDic[ny].add(cnt)
                    land[nx][ny] = cnt
                    queue.append((nx, ny))
                    oil += 1        
        return oil
            
    for i in range(len(land[0])):
        for j in range(len(land)):
            if(land[j][i] == 1):
                dic[cnt] = bfs(j, i)
                cnt += 1
    
    for v in landDic.values():
        tmp = 0
        for i in v:
            tmp += dic[i]
        
        answer = max(answer, tmp)
    
    return answer


'''
from collections import deque
def solution(land):
    answer = []
    
    def bfs(queue):
        visit = [[0]*len(land[0]) for k in range(len(land))]
        pos = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        oil = 0

        while(queue):
            x, y = queue.popleft()
            if(not visit[x][y]):
                visit[x][y] = 1
                oil += 1

            for k in range(4):
                nx = x+pos[k][0]
                ny = y+pos[k][1]

                if 0<=nx<len(land) and 0<=ny<len(land[0]) and visit[nx][ny] == 0 and land[nx][ny]:
                    queue.append((nx, ny))
                    visit[nx][ny] = 1
                    oil += 1
                    
        return oil
            
    for i in range(len(land[0])):
        q = deque()
        for j in range(len(land)):
            if(land[j][i]):
                q.append((j, i))
        answer.append(bfs(q))
    
    return max(answer)
'''