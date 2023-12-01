def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]

    while(True):
        delete = set()
        
        # 지울 블록 위치 찾기
        for i in range(m-1):
            for j in range(n-1):
                if(board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]) and board[i][j] != '0':
                    delete.add((i, j))
                    delete.add((i, j+1))
                    delete.add((i+1, j))
                    delete.add((i+1, j+1))
        answer += len(delete)
        if not delete:
            break
        
        # 블록 삭제
        for pos in delete:
            i, j = pos
            board[i][j] = '0'
        
        # 남은 블록 정리
        for i in range(m-1, -1, -1):
            for j in range(n):
                if(board[i][j] == '0'):
                    tmp = i
                    while(tmp >= 0 and board[tmp][j] == '0'):
                        tmp -= 1
                    if tmp >= 0:
                        board[i][j] = board[tmp][j]
                        board[tmp][j] = '0'
        
    return answer