from collections import defaultdict

def solution(clothes):
    answer = 1
    cDic = defaultdict(int)
    
    for i in clothes:
        cDic[i[1]] += 1
    
    keys = list(cDic.keys())
    for i in keys:
        answer *= (cDic[i]+1)

    return answer-1