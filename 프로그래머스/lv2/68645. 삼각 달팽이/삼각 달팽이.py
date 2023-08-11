def solution(n):
    answer = []
    triList = [[0]*n for i in range(n)]
    x, y = -0, -1
    num = 1
    
    for i in range(n): # n번 반복 -> 3마다 아래 오른쪽 위 순서로 반복
        for j in range(i,n):
            if i % 3 == 0: # 아래
                y += 1
            elif i % 3 == 1: # 오른쪽
                x += 1
            else: # 위
                x -= 1
                y -= 1
            triList[y][x] = num
            num += 1
            
    for i in triList:
        for j in i:
            if j != 0:
                answer.append(j)
            else:
                break
    #print(answer)
    
    return answer