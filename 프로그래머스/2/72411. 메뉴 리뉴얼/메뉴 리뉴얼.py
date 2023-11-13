from itertools import combinations
def solution(orders, course):
    answer = []
    
    for i in course:
        cDic = {}
        for o in orders:
            cList = list(combinations(o, i))
            for c in cList:
                tmp = ''.join(sorted(c))
                if tmp not in cDic:
                    cDic[tmp] = 1
                else:
                    cDic[tmp] += 1
        
        if(cDic):
            m = max(max(cDic.values()), 2)
        
        for key, value in cDic.items():
            if value == m:
                answer.append(key)

    return sorted(answer)