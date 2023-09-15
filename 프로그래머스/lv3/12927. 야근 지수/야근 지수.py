import heapq
def solution(n, works):
    answer = 0
    wh = [-i for i in works]
    heapq.heapify(wh)
    
    for i in range(n):
        w = heapq.heappop(wh) + 1
        heapq.heappush(wh, w)
    
    for i in wh:
        if(i < 0):
            answer += (i ** 2)
    
    return answer