from collections import deque

def solution(board):
    answer = len(board)*len(board)
    pos = [(-1,0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    
    
    def bfs(i, j, ans):
        q = deque()
        q.append((i, j))
        
        while(q):
            x, y = q.popleft()
            board[x][y] = 2
            
            for k in range(8):
                nx = x+pos[k][0]
                ny = y+pos[k][1]
                if ( 0 <= nx < len(board) and 0 <= ny < len(board)) and board[nx][ny] != 2:
                    if(board[nx][ny] == 1):
                        q.append((nx, ny))
                    board[nx][ny] = 2
                    ans -= 1
        return ans
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                answer = bfs(i, j, answer)-1
    
    return answer