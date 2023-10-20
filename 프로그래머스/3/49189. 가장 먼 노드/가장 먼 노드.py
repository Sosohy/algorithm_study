from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for j in range(n+1)]
    visited = [0]*(n+1)
    q = deque()
    
    for i in edge:
        x, y = i
        graph[x].append(y)
        graph[y].append(x)
    
    q.append(1)
    visited[1] = 1
    
    while(q):
        now = q.popleft() 
        
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)
    
    return visited.count(max(visited))