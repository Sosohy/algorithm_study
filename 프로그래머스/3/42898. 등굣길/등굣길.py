def solution(m, n, puddles):
    mapList = [[0 for i in range(m+1)] for j in range(n+1)]
    mapList[1][1] = 1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles: #(m,n)으로 담겨있어서 반대로 
                mapList[i][j] = 0
            else:
                mapList[i][j] += (mapList[i-1][j]+mapList[i][j-1])%1000000007

    return mapList[n][m]