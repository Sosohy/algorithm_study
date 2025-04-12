from collections import deque

def mah(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

for tc in range(int(input())):
    con = int(input())
    posList = [list(map(int, input().split())) for i in range(con+2)]
    visited = [0]*(con+2)
    visited[0] = 1

    q = deque([posList[0]])

    while(q):
        now = q.popleft()

        for i in range(con+2):
            if(visited[i] == 0 and mah(now, posList[i]) <= 1000):
                if(i == con+1):
                    visited[i] = 1
                    break
                q.append(posList[i])
                visited[i] = 1
        
    if(visited[-1] == 1):
        print("happy")
    else:
        print("sad")
