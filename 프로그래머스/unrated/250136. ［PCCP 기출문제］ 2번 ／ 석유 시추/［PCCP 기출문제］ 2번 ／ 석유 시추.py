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