from collections import deque

n = int(input()) + 1
com = [[0]*n for i in range(n)]

for i in range(int(input())):
    s, e = map(int, input().split())
    com[s][e] = 1
    com[e][s] = 1

def bfs(t):
    answer = 0
    visited = [0]*n
    visited[t] = 1

    vir = deque()
    vir.append(t)

    while(vir):
        m = vir.popleft()
        for i in range(1, n):
            if(com[m][i] == 1 and visited[i] == 0):
                vir.append(i)
                visited[i] = 1
                answer += 1

    return answer

print(bfs(1))