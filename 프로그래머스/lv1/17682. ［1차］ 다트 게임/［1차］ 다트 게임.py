def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    darts = []
    score = ''
    
    for i in dartResult:
        
        if (i.isdigit()):
            score += str(i)
        elif (i in bonus):
            darts.append(pow(int(score), bonus[i]))
            score = ''
        elif (i == '*'):
            darts[-1] = darts[-1]*2
            if(len(darts) > 1):
                darts[-2] = darts[-2]*2
        else:
            darts[-1] = darts[-1]*-1

    return sum(darts)