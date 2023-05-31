import heapq

def solution(operations):
    answer = []
    cal = []
    
    for i in operations:
        tmp = i.split()
        
        if tmp[0] == 'I':
            heapq.heappush(cal, int(tmp[1]))
        elif tmp[0] == 'D' and cal:
            if (tmp[1] == '-1'):
                heapq.heappop(cal)
            else:
                cal.pop(-1)
                
    if cal:
        cal.sort()
        return [cal[-1], cal[0]]
        
    return [0, 0]