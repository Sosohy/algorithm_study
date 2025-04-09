from collections import deque

n = int(input())+1
m, c = map(int, input().split())
nList = [[0]*n for i in range(n)]

for i in range(int(input())):
    s, e = map(int, input().split())
    nList[s][e] = 1
    nList[e][s] = 1

def bfs(start, end):
    visited = [-1]*n
    q = deque()
    q.append((start, 0))
    visited[start] = 1
    cnt = 0

    while(q):
        st, c = q.popleft()
        for k in range(1, n):
            if(nList[st][k] == 1 and visited[k] == -1):
                if(k == end):
                    return c+1
                q.append((k, c+1))
                visited[k] = 1
    return -1
    
print(bfs(m, c))
