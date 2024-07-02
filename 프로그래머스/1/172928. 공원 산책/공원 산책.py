def solution(park, routes):
    answer = []
    
    dog = [0, 0]
    direction = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    
    for i in range(len(park)):
        if('S' in park[i]):
            dog = (i, park[i].index('S'))
            break

    for i in routes:
        op, n = i.split(" ") 
        h, w = direction[op]
        
        dirH, dirW = dog[0], dog[1]
        for j in range(int(n)):
            dirH += h
            dirW += w
            if((0 <= dirH < len(park) and 0 <= dirW < len(park[0]) 
                 and park[dirH][dirW] != 'X') == False):
                dirH, dirW = dog[0], dog[1]
                break;
                
        dog = [dirH, dirW]
    
    return dog