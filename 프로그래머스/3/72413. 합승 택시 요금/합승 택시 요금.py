def solution(n, s, a, b, fares):
    INF = 9999999
    answer = INF
    fare = [[INF for i in range(n)] for j in range(n)]
    
    for i in range(n):
        fare[i][i] = 0
        
    for i in fares:
        n1, n2, f = i
        fare[n1-1][n2-1] = f
        fare[n2-1][n1-1] = f
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(fare[i][k]+fare[k][j] < fare[i][j]):
                    fare[i][j] = fare[i][k]+fare[k][j]
                    
    a, b, s = a-1, b-1, s-1
    for k in range(n):
        if(answer > fare[s][k]+fare[k][a]+fare[k][b]):
            answer = fare[s][k]+fare[k][a]+fare[k][b]

    return answer