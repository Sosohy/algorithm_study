def solution(want, number, discount):
    answer = 0
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for i in range(10):
        if(discount[i] in dic):
            dic[discount[i]] -= 1
    
    def isTrue():
        for key in list(dic.keys()):
            if(dic[key] > 0):
                return False
                break
            
        return True
            
    if(isTrue()):
        answer += 1

    for i in range(10, len(discount)):
        
        if(discount[i-10] in dic):
            dic[discount[i-10]] += 1
        
        if(discount[i] in dic):
            dic[discount[i]] -= 1
        
        if(isTrue()):
            answer += 1
    
    return answer