from itertools import combinations

def solution(clothes):
    answer = 1
    
    closetDic = {}
    
    for i in clothes:
        if (i[1] in closetDic):
            closetDic[i[1]].append(i[0])
        else:
            closetDic[i[1]] = [i[0]]
            
    for i in closetDic.keys():
        answer *= (len(closetDic[i])+1)
        print(i, closetDic[i])
    
    return answer-1