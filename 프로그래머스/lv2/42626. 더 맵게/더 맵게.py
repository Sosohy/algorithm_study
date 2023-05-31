import heapq

def solution(scoville, K):
    answer = 0
    
    if K == 0:
        return 0
    
    heapq.heapify(scoville)
    scoMin = heapq.heappop(scoville)
    
    while scoville:
        if scoMin >= K:
            break
            
        new = scoMin + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, new)
        answer += 1
        scoMin = heapq.heappop(scoville)

    if scoMin >= K:
        return answer
    
    return -1