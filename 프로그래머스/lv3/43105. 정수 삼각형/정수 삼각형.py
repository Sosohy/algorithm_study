def solution(triangle):
    sList = [[0 for i in range(len(triangle))] for j in range(len(triangle))]
    
    sList[0][0] = triangle[0][0]
    for i in range(0, len(triangle)-1):
            for j in range(len(triangle[i])):
                sList[i+1][j] = max(sList[i+1][j], sList[i][j]+triangle[i+1][j])
                sList[i+1][j+1] = max(sList[i+1][j+1], sList[i][j]+triangle[i+1][j+1])
                
    answer = max(sList[len(triangle)-1])
    
    return answer