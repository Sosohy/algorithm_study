def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for i in tangerine:
        if(i not in dic):
            dic[i] = 0
        dic[i] += 1
    
    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    
    s = 0
    for i in dic.keys():
        answer += 1
        s += dic[i]
        if(s >= k):
            return answer
    
    return answer