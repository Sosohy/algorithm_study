def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    
    for i in range(n, -1, -1):
        tmp = 0
        for j in range(n):
            if(citations[j] >= i):
                tmp += 1
        if(tmp >= i and n-tmp <= i):
            answer = i
            break
        
    return answer