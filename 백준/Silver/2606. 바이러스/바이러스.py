from collections import deque

n = int(input())
m = int(input())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    c1, c2 = map(int, input().split())
    graph[c1][c2] = 1
    graph[c2][c1] = 1

def dfs(v):
    visited[v] = 1

    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

bfs(1)
print(visited.count(1) - 1)