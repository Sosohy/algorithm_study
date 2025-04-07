def solution(wallpaper):
    answer = []
    pos1, pos2 = [51, 51], [-1, -1]
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if(wallpaper[i][j] == '#'):
                pos1[0] = min(pos1[0], i)
                pos1[1] = min(pos1[1], j)
                    
                pos2[0] = max(pos2[0], i)
                pos2[1] = max(pos2[1], j)

    answer = [pos1[0], pos1[1], pos2[0]+1, pos2[1]+1]
    return answer