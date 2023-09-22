def DFS(i, computers, visited):
    visited[i] = 1
    for j in range(len(computers)):
        if computers[i][j] == 1 and visited[j] == 0:
            DFS(j, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            DFS(i, computers, visited)
            answer += 1
    
    return answer