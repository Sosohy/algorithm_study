from collections import deque
def solution(maps):
    game = [[-1 for j in range(len(maps[0]))] for i in range(len(maps))]
    queue = deque()
    queue.append((0, 0, 1))
    game[0][0] = 1
    
    dirList = [(-1,0), (0, 1), (1, 0), (0, -1)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        for i in range(4):
            dx = dirList[i][0] + x
            dy = dirList[i][1] + y
            
            if (0 <= dx < len(maps)) and (0 <= dy < len(maps[0])) and maps[dx][dy] == 1:
                if game[dx][dy] == -1 or (dist+1 < game[dx][dy]):
                    game[dx][dy] = dist+1
                    queue.append((dx, dy, dist+1))
    
    return game[len(maps)-1][len(maps[0])-1]