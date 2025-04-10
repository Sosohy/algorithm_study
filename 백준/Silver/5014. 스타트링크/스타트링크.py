from collections import deque

f1, s1, g1, u1, d1 = map(int, input().split())

def bfs(f, gang, company, u, d):
    visited = [0]*(f+1)
    q = deque([(gang, 0)])
    visited[gang] = 1

    while(q):
        x, cnt = q.popleft()
        if(x == company):
            return cnt

        for i in [u, -d]:
            nx = x+i
            if(0 < nx <= f and visited[nx] == 0):
                q.append((nx, cnt+1))
                visited[nx] = 1
    
    return "use the stairs"

print(bfs(f1, s1, g1, u1, d1))
