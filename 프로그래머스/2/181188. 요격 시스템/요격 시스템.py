def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[1])
    m = targets[0]
    
    for i in range(1, len(targets)):
        if(targets[i][0] >= m[1]):
            m = targets[i]
            answer += 1
        
    return answer