from collections import deque

def solution(points, routes):
    answer = 0
    routeList = []

    def checkRoute(points, routes):
        for i in range(len(routes)):
            r = deque() # 로봇마다 이동 경로 저장

            # routes[i] => (시작 포인트, 방문 포인트, ... , 끝 포인트)
            start = points[routes[i][0]-1]
            x, y = start[0], start[1]
            r.append((x, y))
            
            for j in range(len(routes[0])):
                end = points[routes[i][j]-1]
                dx, dy = end[0], end[1]

                nx, ny = dx-x, dy-y
                while(nx != 0):
                    if(nx > 0):
                        x += 1
                        nx -= 1
                    else:
                        x -= 1
                        nx += 1
                    r.append((x, y))

                while(ny != 0):
                    if(ny > 0):
                        y += 1
                        ny -= 1
                    else:
                        y -= 1
                        ny += 1
                    r.append((x, y))
            routeList.append(r)
    
    def checkCollide(routeList):
        empty = 0
        cnt = 0

        while(empty < len(routes)):
            empty = 0
            mapList = [[0]*101 for _ in range(101)]
            
            for i in range(len(routes)):
                if not routeList[i]:
                    empty += 1
                    continue
                
                nx, ny = routeList[i].popleft()
                mapList[nx][ny] += 1
            
            for i in range(1, 101):
                for j in range(1, 101):
                    if(mapList[i][j] > 1):
                        cnt += 1
            
        return cnt

    checkRoute(points, routes)
    answer = checkCollide(routeList)

    return answer