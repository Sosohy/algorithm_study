def solution(wallpaper):
    answer = []
    lx, ly = len(wallpaper), len(wallpaper[0])
    rx, ry = -1, -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j] == '#'):
                lx = min(i, lx)
                ly = min(j, ly)
                rx = max(i, rx)
                ry = max(j, ry)
                
    answer = [lx,ly,rx+1,ry+1]
    return answer