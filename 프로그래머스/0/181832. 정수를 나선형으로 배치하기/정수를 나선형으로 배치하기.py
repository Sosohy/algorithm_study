def solution(n):
    answer = [[0]*n for i in range(n)]
    
    x, y = 0, 0
    nDir = 0 # →, ↓, ←, ↑
    
    for i in range(n*n):
        answer[x][y] = i+1
        
        if(n == 1):
            return answer
        
        if(nDir%4 == 0): # 왼쪽 -> 오른쪽
            y += 1
            if(y == n-1 or answer[x][y+1] != 0):
                nDir += 1
        elif(nDir%4 == 1): # 위 -> 아래
            x += 1
            if(x == n-1 or answer[x+1][y] != 0):
                nDir += 1
        elif(nDir%4 == 2): # 오른쪽 -> 왼쪽
            y -= 1
            if(y == 0 or answer[x][y-1] != 0):
                nDir += 1
        elif(nDir%4 == 3): # 아래 -> 위
            x -= 1
            if(answer[x-1][y] != 0):
                nDir += 1
            
    return answer