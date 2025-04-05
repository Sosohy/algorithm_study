def solution(board, h, w):
    answer = 0
    pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    for i in pos:
        nh = h + i[0]
        nw = w + i[1]
        
        if(0 <= nh < len(board) and 0 <= nw < len(board[0])):
            if(board[h][w] == board[nh][nw]):
                answer += 1    
    
    return answer