def solution(priorities, location):
    work = 0
    i = 0
    finish = 0
    
    while finish <= len(priorities):
        while True:
            start = work
            if (priorities[work] < priorities[i]):
                work = i
            else:
                i = (i+1) % len(priorities)
            
            if (i == start): break

        finish += 1
        priorities[work] = -1
        
        if(work == location):
            return finish

    return len(priorities)