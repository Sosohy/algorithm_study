def solution(k, m, score):
    answer = 0
    
    score.sort(reverse = True)
    idx = m-1
    
    while(idx < len(score)):
        sc = score[idx]
        answer += (sc * m)
        
        idx += m
    
    return answer