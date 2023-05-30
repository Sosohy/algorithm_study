def solution(priorities, location):
    work = 0
    i = 0
    finish = []
    
    while len(finish) <= len(priorities):
        while True:
            start = work
            if (priorities[work] < priorities[i]):
                work = i
            else:
                i = (i+1) % len(priorities)
            
            if (i == start): break
                   
        finish.append(work)
        priorities[work] = -1
        
        if(work == location):
            return len(finish)
    
    return len(priorities)