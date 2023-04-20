def solution(dirs):
    dirDict = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    path = set()
    x, y = 0, 0
    
    for i in dirs:
        nx = x + dirDict[i][0]
        ny = y + dirDict[i][1]
        
        if (-5 <= nx <= 5) and (-5 <= ny <= 5):
            path.add(((x, y), (nx, ny))) # 현재 좌표, 이동 좌표
            path.add(((nx, ny), (x, y))) # 이동 좌표, 현재 좌표
            x, y = nx, ny # 이동 했으니까 현재 위치 업데이트
    
    return len(path)//2