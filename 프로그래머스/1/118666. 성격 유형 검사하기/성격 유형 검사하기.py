def solution(survey, choices):
    answer = ''
    dicType = {"R":0, "T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    for i in range(len(survey)):
        sType = survey[i] 
        score = choices[i]
        
        if(score <= 4):
            dicType[sType[0]] += 4-score
        else:
            dicType[sType[1]] += score-4
    
    typeKey = list(dicType.keys())
    for i in range(0, len(typeKey), 2):
        if(dicType[typeKey[i]] >= dicType[typeKey[i+1]]):
            answer += typeKey[i]
        else:
            answer += typeKey[i+1]
    
    return answer