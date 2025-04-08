def solution(participant, completion):
    answer = ''
    dic = {}
    
    for i in participant:
        if(i not in dic):
            dic[i] = 0
        dic[i] += 1
        
    for i in completion:
        dic[i] -= 1
    
    keys = list(dic.keys())
    for i in keys:
        if(dic[i] != 0):
            answer = i
    
    return answer