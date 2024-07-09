def solution(participant, completion):
    answer = ''
    m = {}
    
    for i in participant:
        if(i not in m):
            m[i] = 0
        m[i] += 1
    
    for i in completion:
        m[i] -= 1
    
    for k, v in m.items():
        if(m[k] != 0):
            return k
    
    return answer