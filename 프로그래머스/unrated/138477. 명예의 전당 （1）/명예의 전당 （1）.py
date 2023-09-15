import heapq
def solution(k, score):
    answer = []
    rank = []
    
    for i in score:
        if(len(rank) < k):
            heapq.heappush(rank, i)
        else:
            heapq.heappush(rank, i)
            heapq.heappop(rank)
        answer.append(rank[0])
    
    return answer