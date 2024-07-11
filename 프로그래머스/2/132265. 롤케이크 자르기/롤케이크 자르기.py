from collections import Counter

def solution(topping):
    answer = 0
    chulDic = Counter(topping)
    broDic = {}
    
    for i in topping:
        if(i not in broDic):
            broDic[i] = 0
        broDic[i] += 1
        
        chulDic[i] -= 1
        if(chulDic[i] == 0):
            chulDic.pop(i)
        
        if(len(broDic) == len(chulDic)):
            answer += 1
        
    return answer