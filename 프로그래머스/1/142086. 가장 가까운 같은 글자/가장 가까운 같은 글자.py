def solution(s):
    answer = []
    aList = {}
    
    for i in range(len(s)):
        if(s[i] not in aList):
            answer.append(-1)
            aList[s[i]] = i
        else:
            answer.append(i-aList[s[i]])
            aList[s[i]] = i
        
    return answer