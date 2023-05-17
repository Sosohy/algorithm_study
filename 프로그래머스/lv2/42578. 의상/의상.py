def solution(clothes):
    answer = 1
    
    closetDic = {}
    
    for i in clothes:
        if (i[1] in closetDic):
            closetDic[i[1]].append(i[0])
        else:
            closetDic[i[1]] = [i[0]]
            
    for i in closetDic.values():
        answer *= (len(i)+1)
        print(i)
    
    return answer-1