def solution(dartResult):
    answer = 0
    dart = []
    n = 0
    
    while(n < len(dartResult)):
        i = dartResult[n]
        if(i.isnumeric()):
            if(dartResult[n+1].isnumeric()):
                dart.append(int(i+dartResult[n+1]))
                n = n+1
            else:
                dart.append(int(i))
        elif(i in ['S', 'D', 'T']):
            if(i == 'D'):
                dart[-1] = dart[-1]**2
            elif(i == 'T'):
                dart[-1] = dart[-1]**3
        else:
            if(i=='*'):
                dart[-1] = dart[-1]*2
                if(len(dart) >= 2):
                    dart[-2] = dart[-2]*2
            else:
                dart[-1] = -dart[-1]
        n = n+1

    return sum(dart)