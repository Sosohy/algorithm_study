import heapq

def solution(jobs):
    answer = 0
    
    now = 0
    fin = 0
    start = -1
    heap = []
    
    while fin < len(jobs):
        for i in jobs:
            if start < i[0] <= now: 
                heapq.heappush(heap, [i[1], i[0]]) 
        
        if len(heap) > 0: 
            work = heapq.heappop(heap) 
            start = now
            now += work[0]
            answer += (now - work[1])
            fin += 1
        else: 
            now += 1
    
    return answer // len(jobs)