def solution(k, tangerine):
    answer = 0
    typeDic = {}
    
    for i in tangerine:
        if(i not in typeDic):
            typeDic[i] = 0
        typeDic[i] += 1
    
    values = list(typeDic.values())
    values.sort(reverse=True)
    
    for i in values:
        if(k <= 0):
            return answer
        
        answer += 1
        k -= i
        
    return answer