from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0]*(n+1) for j in range(n+1)]
visited = [0]*(n+1)

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')

    for u in range(1, n+1):
        if graph[v][u] == 1 and not visited[u]:
            dfs(u)
  
def bfs(s):
    visited = [0 for i in range(n+1)]
    queue = deque([s])
    visited[s] = 1
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for u in range(1, n+1):
            if graph[v][u] == 1 and not visited[u]:
                visited[u] = 1
                queue.append(u)
                
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
print()
bfs(v)