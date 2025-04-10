from collections import deque

sn, sk = map(int, input().split())

def bfs(n, k):
    visited = [0]*100001
    ans = 100001
    q = deque([(n, 0)])
    pos = []

    while(q):
        x, time = q.popleft()
        
        if(x == k):
            return time

        for i in [x-1, x+1, x*2]:
            if( 0 <= i <= 100000 and visited[i] == 0):
                q.append((i, time+1))
                visited[i] = 1
    return ans

print(bfs(sn, sk))