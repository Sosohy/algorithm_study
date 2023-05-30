def solution(priorities, location):
    work = 0
    i = 0
    finish = 0
    
    while finish <= len(priorities):
        while True:
            if (priorities[work] < priorities[i]):
                work = i
            else:
                i = (i+1) % len(priorities)
            
            if priorities[work] == max(priorities): break

        finish += 1
        priorities[work] = -1
        
        if(work == location):
            return finish

    return len(priorities)