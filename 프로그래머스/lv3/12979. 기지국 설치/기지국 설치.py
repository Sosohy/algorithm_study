import math

def solution(n, stations, w):
    answer = 0
    
    start = 1
    for i in stations:
        apt = (i-w)-start
        if apt > 0:
            answer += math.ceil(apt/(2*w + 1))
        start = (i+w)+1
        
    if n >= start:
        answer += math.ceil((n-start+ 1)/(2*w + 1))

    return answer