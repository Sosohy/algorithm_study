def solution(survey, choices):
    answer = ''
    dicType = {"R":0, "T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    for i, j in zip(survey, choices):
        disagree = i[0]
        agree = i[1]
        
        if(j<= 4): #비동의
            dicType[disagree] += 4-j
        else: #동의
            dicType[agree] += j-4
        
    keys = list(dicType.keys())
    for i in range(0, len(keys), 2):
        if(dicType[keys[i]] >= dicType[keys[i+1]]):
            answer += keys[i]
        else:
            answer += keys[i+1]
    
    return answer