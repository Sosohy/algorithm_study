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
            dx, dy = dirList[i]
            if (0 <= dx+x < len(maps)) and (0 <= dy+y < len(maps[0])) and maps[dx+x][dy+y] == 1:
                if game[dx+x][dy+y] == -1 or (dist+1 < game[dx+x][dy+y]):
                    game[dx+x][dy+y] = dist+1
                    queue.append((dx+x, dy+y, dist+1))
    
    return game[len(maps)-1][len(maps[0])-1]